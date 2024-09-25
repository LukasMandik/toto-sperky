from django.db import models
from django.urls import reverse
from django.urls import reverse
from PIL import Image
from moviepy.editor import VideoFileClip
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import os
import os
import tempfile
from moviepy.editor import VideoFileClip
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
import cv2
import sys
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
# Create your models here.
from django.db import models
from django.core.files.base import ContentFile
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from PIL import Image
from io import BytesIO
from moviepy.editor import VideoFileClip
import cv2
import warnings

class Blog(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'blogs'
        ordering = ('-created',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('toto_sperky_web:blog_detail', args=[self.slug])
    

    def reading_time(self):
        # Priemerná rýchlosť čítania je okolo 220 slov za minútu
        words_per_minute = 200
        # Rozdelenie textu na slová
        word_count = len(self.description.split())
        # Vypočítať čas čítania v minútach a sekundách
        reading_time_minutes = word_count / words_per_minute
        reading_time_seconds = (reading_time_minutes * 60) % 60
        # Zaokrúhlenie sekúnd na najbližších 10 sekúnd
        rounded_seconds = round(reading_time_seconds / 10) * 10
        # Vypočítať celkový čas čítania v minútach a sekundách
        total_minutes = int(reading_time_minutes)
        if rounded_seconds == 60:
            total_minutes += 1
            rounded_seconds = 0
        # Vrátiť čas čítania vo formáte minúty:sekundy
        return f"{total_minutes} m {rounded_seconds} s"


class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    image_thumbnail = models.ImageField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.image:
            with Image.open(self.image) as img:
                # Získanie veľkosti súboru v bajtoch
                file_size = self.image.size
                print("Before saving image:", self.image.width, self.image.height, self.image.size / (1024 * 1024), "MB")
                if file_size > 2 * 1024 * 1024:  # 2 MB prevedené na bajty
                    # Získanie pôvodných rozmerov obrázku
                    orig_width, orig_height = img.size
                    # Zistenie orientácie obrázku
                    if orig_width > orig_height:
                        # Zmena veľkosti na max. 1200x...
                        new_width = 1200
                        new_height = int((orig_height / orig_width) * new_width)
                    else:
                        # Zmena veľkosti na max. ...x1200
                        new_height = 1200
                        new_width = int((orig_width / orig_height) * new_height)
                    img.thumbnail((new_width, new_height), Image.LANCZOS)
                    buffer = BytesIO()
                    img.save(buffer, format='PNG')
                    self.image = InMemoryUploadedFile(buffer, None, f"{self.image.name.split('.')[0]}_compressed.png", 'image/png', buffer.tell(), None)
                print("After saving image:", self.image.width, self.image.height, self.image.size / (1024 * 1024), "MB")
                if self.image_thumbnail:
                    if self.image_thumbnail.name != f"{self.image.name.split('.')[0]}_thumbnail.png": 
                        img.thumbnail((300, 300), Image.LANCZOS)
                        thumbnail_buffer = BytesIO()
                        img.save(thumbnail_buffer, format='PNG')
                        self.image_thumbnail.save(f"{self.image.name.split('.')[0]}_thumbnail.png", ContentFile(thumbnail_buffer.getvalue()), save=False)
                        print("After saving image thumbnail:", self.image_thumbnail.width, self.image_thumbnail.height, self.image_thumbnail.size / (1024 * 1024), "MB")
                else:
                    img.thumbnail((300, 300), Image.LANCZOS)
                    thumbnail_buffer = BytesIO()
                    img.save(thumbnail_buffer, format='PNG')
                    self.image_thumbnail.save(f"{self.image.name.split('.')[0]}_thumbnail.png", ContentFile(thumbnail_buffer.getvalue()), save=False)
                    print("After saving image thumbnail:", self.image_thumbnail.width, self.image_thumbnail.height, self.image_thumbnail.size / (1024 * 1024), "MB")
        if not self.image:
            self.image_thumbnail = None
        super().save(*args, **kwargs)

@receiver(pre_save, sender=BlogImage)
def update_blog_image_thumbnails(sender, instance, **kwargs):
    if not instance.image:
        instance.image_thumbnail = None





class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(blank=True, null=True,)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Zpracování obrázku
        if self.image:
            # Vytvoření náhledového obrázku
            with Image.open(self.image) as img:
                # Získanie veľkosti súboru v bajtoch
                file_size = self.image.size
                print("Before saving image:", self.image.width, self.image.height, self.image.size / (1024 * 1024), "MB")
                if file_size > 0.1 * 1024 * 1024:  # 0.1 MB prevedené na bajty
                        # Získání původních rozměrů obrázku
                        orig_width, orig_height = img.size
                        # Zjistit orientaci obrazku
                        if orig_width > orig_height:
                            # Zmenit velikost na max. 1200x...
                            new_width = 220
                            new_height = int((orig_height / orig_width) * new_width)
                        else:
                            # Zmenit velikost na max. ...x1200
                            new_height = 220
                            new_width = int((orig_width / orig_height) * new_height)
                        img.thumbnail((new_width, new_height), Image.LANCZOS)
                        buffer = BytesIO()
                        img.save(buffer, format='PNG')
                        self.image = InMemoryUploadedFile(buffer, None, f"{self.image.name.split('.')[0]}_category_thumbnail.png", 'image/png', buffer.tell(), None)
                        print("After saving image:", self.image.width, self.image.height, self.image.size / (1024 * 1024), "MB")
        super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(null=True, blank=True)
    video = models.FileField(null=True, blank=True)   # Nové pole pro video soubor
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    
    # Nové pole pro náhledový obrázek videa
    video_thumbnail = models.FileField(null=True, blank=True)
    
    # Nové pole pro náhledový obrázek produktu
    image_thumbnail = models.ImageField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('toto_sperky_web:product_detail', args=[self.slug])

    class Meta:
        verbose_name_plural = 'products'
        ordering = ('-created',)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        # Zpracování obrázku
        if self.image:
            # Print original image size
            print("Original image size (before processing):", self.image.size / (1024 * 1024), "MB")
            
            with Image.open(self.image) as img:
                file_size = self.image.size
                print("Before saving image:", self.image.width, self.image.height, file_size / (1024 * 1024), "MB")
                
                if file_size > 2 * 1024 * 1024:
                    orig_width, orig_height = img.size
                    if orig_width > orig_height:
                        new_width = 1200
                        new_height = int((orig_height / orig_width) * new_width)
                    else:
                        new_height = 1200
                        new_width = int((orig_width / orig_height) * new_height)
                    img.thumbnail((new_width, new_height), Image.LANCZOS)
                    buffer = BytesIO()
                    img.save(buffer, format='PNG')
                    self.image = InMemoryUploadedFile(buffer, None, f"{self.image.name.split('.')[0]}_compressed.png", 'image/png', buffer.tell(), None)
                
                print("After saving image:", self.image.width, self.image.height, self.image.size / (1024 * 1024), "MB")

                if self.image_thumbnail:
                    if self.image_thumbnail.name != f"{self.image.name.split('.')[0]}_thumbnail.png":
                        img.thumbnail((300, 300), Image.LANCZOS)
                        thumbnail_buffer = BytesIO()
                        img.save(thumbnail_buffer, format='PNG')
                        self.image_thumbnail.save(f"{self.image.name.split('.')[0]}_thumbnail.png", ContentFile(thumbnail_buffer.getvalue()), save=False)
                        print("After saving image thumbnail:", self.image_thumbnail.width, self.image_thumbnail.height, self.image_thumbnail.size / (1024 * 1024), "MB")
                else:
                    img.thumbnail((300, 300), Image.LANCZOS)
                    thumbnail_buffer = BytesIO()
                    img.save(thumbnail_buffer, format='PNG')
                    self.image_thumbnail.save(f"{self.image.name.split('.')[0]}_thumbnail.png", ContentFile(thumbnail_buffer.getvalue()), save=False)
                    print("After saving image thumbnail:", self.image_thumbnail.width, self.image_thumbnail.height, self.image_thumbnail.size / (1024 * 1024), "MB")

        # Save the product instance to create a file path for the video
        super().save(*args, **kwargs)

        # Zpracování videa

        if self.video:
            video_path = self.video.path
            print("Original video size (before processing):", os.path.getsize(video_path) / (1024 * 1024), "MB")
            
            base_name, ext = os.path.splitext(os.path.basename(video_path))

            # Skontrolujte, či video už má koncovku _compressed
            if '_compressed' in base_name:
                print("Video is already compressed, skipping compression.")
            else:
                try:
                    video = VideoFileClip(video_path)
                    print("Original video dimensions:", video.size)

                    # Define paths for the compressed video and thumbnail
                    compressed_video_path = os.path.join(os.path.dirname(video_path), f"{base_name}_compressed{ext}")
                    thumbnail_video_path = os.path.join(os.path.dirname(video_path), f"{base_name}_thumbnail{ext}")

                    # Video compression
                    if video.size[0] > 1280 or video.size[1] > 720:
                        # Calculate new dimensions while preserving aspect ratio
                        aspect_ratio = video.size[0] / video.size[1]
                        if video.size[0] > video.size[1]:
                            new_width = 1280
                            new_height = int(1280 / aspect_ratio)
                        else:
                            new_height = 720
                            new_width = int(720 * aspect_ratio)
                        
                        video = video.resize(newsize=(new_width, new_height))
                        video.write_videofile(compressed_video_path, codec='libx264', bitrate='5000k')
                        self.video = ContentFile(open(compressed_video_path, 'rb').read(), name=f"{base_name}_compressed{ext}")
                        print("Video compressed and saved as:", compressed_video_path)
                        print("Compressed video size:", os.path.getsize(compressed_video_path) / (1024 * 1024), "MB")
                        print("Compressed video dimensions:", (new_width, new_height))
                    else:
                        self.video = ContentFile(open(video_path, 'rb').read(), name=f"{base_name}_compressed{ext}")
                        print("Video size is acceptable, no compression needed.")

                    # Generate video thumbnail
                    if not self.video_thumbnail or self.video_thumbnail.name != f"{base_name}_thumbnail{ext}":
                        thumbnail_clip = video.subclip(0, min(10, video.duration))  # Extract the first 10 seconds or the length of the video
                        thumbnail_clip.write_videofile(thumbnail_video_path, codec='libx264', bitrate='500k')
                        new_thumbnail_file = ContentFile(open(thumbnail_video_path, 'rb').read(), name=f"{base_name}_thumbnail{ext}")

                        # Save new thumbnail if it is different from the current one
                        if not self.video_thumbnail or self.video_thumbnail.name != new_thumbnail_file.name:
                            self.video_thumbnail.save(f"{base_name}_thumbnail{ext}", new_thumbnail_file, save=False)
                            print("Video thumbnail created and saved as:", self.video_thumbnail.name)
                            print("Thumbnail video size:", os.path.getsize(thumbnail_video_path) / (1024 * 1024), "MB")

                    # Clean up temporary files
                    for path in [compressed_video_path, thumbnail_video_path]:
                        if os.path.exists(path):
                            os.remove(path)
                except Exception as e:
                    print(f"An error occurred during video processing: {e}")
                    warnings.warn(f"An error occurred during video processing: {e}")

        if not self.image:
            self.image_thumbnail = None
        if not self.video:
            self.video_thumbnail = None

        super().save(*args, **kwargs)


@receiver(pre_save, sender=Product)
def update_product_images(sender, instance, **kwargs):
    if not instance.image:
        instance.image_thumbnail = None








