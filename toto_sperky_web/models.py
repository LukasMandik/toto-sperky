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
from moviepy.editor import VideoFileClip
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.db import models
from django.core.files.base import ContentFile
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from PIL import Image
from io import BytesIO
from moviepy.editor import VideoFileClip
import cv2
from PIL import ExifTags
import subprocess
from django.core.cache import cache
from ffmpeg_progress_yield import FfmpegProgress
import logging

logger = logging.getLogger(__name__)

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
    
        # Meta informácie pre django-meta
    def get_meta_title(self):
        return self.name

    def get_meta_description(self):
        return f"Prečítajte si viac o {self.name} na našom blogu. {self.description[:150]}..."

    def get_meta_image(self):
        return self.images.first().image.url if self.images.first() else None


class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    image_thumbnail = models.ImageField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.image:
            with Image.open(self.image) as img:
                # Oprava orientácie podľa EXIF
                try:
                    for orientation in ExifTags.TAGS.keys():
                        if ExifTags.TAGS[orientation] == 'Orientation':
                            break
                    exif = img._getexif()
                    if exif is not None:
                        orientation = exif.get(orientation, None)
                        if orientation == 3:
                            img = img.rotate(180, expand=True)
                        elif orientation == 6:
                            img = img.rotate(270, expand=True)
                        elif orientation == 8:
                            img = img.rotate(90, expand=True)
                except (AttributeError, KeyError, IndexError):
                    # prípad, keď obrázok nemá EXIF informácie
                    pass

                # Zvyšok vášho kódu pre spracovanie obrázku
                file_size = self.image.size
                print("Before saving image:", img.width, img.height, file_size / (1024 * 1024), "MB")
                
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
                
                print("After saving image:", img.width, img.height, self.image.size / (1024 * 1024), "MB")

                if self.image_thumbnail:
                    if self.image_thumbnail.name != f"{self.image.name.split('.')[0]}_thumbnail.png":
                        img.thumbnail((600, 600), Image.LANCZOS)
                        thumbnail_buffer = BytesIO()
                        img.save(thumbnail_buffer, format='PNG')
                        self.image_thumbnail.save(f"{self.image.name.split('.')[0]}_thumbnail.png", ContentFile(thumbnail_buffer.getvalue()), save=False)
                        print("After saving image thumbnail:", self.image_thumbnail.width, self.image_thumbnail.height, self.image_thumbnail.size / (1024 * 1024), "MB")
                else:
                    img.thumbnail((600, 600), Image.LANCZOS)
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
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'categories'
    
    def get_absolute_url(self):
        return reverse('toto_sperky_web:category_detail', args=[self.slug])

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Zpracování obrázku
        if self.image:
            with Image.open(self.image) as img:
                # Oprava orientácie podľa EXIF
                try:
                    for orientation in ExifTags.TAGS.keys():
                        if ExifTags.TAGS[orientation] == 'Orientation':
                            break
                    exif = img._getexif()
                    if exif is not None:
                        orientation = exif.get(orientation, None)
                        if orientation == 3:
                            img = img.rotate(180, expand=True)
                        elif orientation == 6:
                            img = img.rotate(270, expand=True)
                        elif orientation == 8:
                            img = img.rotate(90, expand=True)
                except (AttributeError, KeyError, IndexError):
                    # prípad, keď obrázok nemá EXIF informácie
                    pass

                # Získanie veľkosti súboru v bajtoch
                file_size = self.image.size
                print("Before saving image:", img.width, img.height, file_size / (1024 * 1024), "MB")
                if file_size > 0.1 * 1024 * 1024:  # 0.1 MB prevedené na bajty
                    # Získání původních rozměrů obrázku
                    orig_width, orig_height = img.size
                    # Zjistit orientaci obrazku
                    if orig_width > orig_height:
                        # Zmenit velikost na max. 220x...
                        new_width = 220
                        new_height = int((orig_height / orig_width) * new_width)
                    else:
                        # Zmenit velikost na max. ...x220
                        new_height = 220
                        new_width = int((orig_width / orig_height) * new_height)
                    img.thumbnail((new_width, new_height), Image.LANCZOS)
                    buffer = BytesIO()
                    img.save(buffer, format='PNG')
                    self.image = InMemoryUploadedFile(buffer, None, f"{self.image.name.split('.')[0]}_category_thumbnail.png", 'image/png', buffer.tell(), None)
                    print("After saving image:", img.width, img.height, self.image.size / (1024 * 1024), "MB")
        super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(null=True, blank=True)
    video = models.FileField(null=True, blank=True) 
    video_webm = models.FileField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    
    # Nové pole pro náhledový obrázek videa
    video_thumbnail = models.FileField(null=True, blank=True)
    
    # Nové pole pro náhledový obrázek produktu
    image_thumbnail = models.ImageField(null=True, blank=True)
    progress = models.IntegerField(default=0)

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
                # Oprava orientácie podľa EXIF
                try:
                    for orientation in ExifTags.TAGS.keys():
                        if ExifTags.TAGS[orientation] == 'Orientation':
                            break
                    exif = img._getexif()
                    if exif is not None:
                        orientation = exif.get(orientation, None)
                        if orientation == 3:
                            img = img.rotate(180, expand=True)
                        elif orientation == 6:
                            img = img.rotate(270, expand=True)
                        elif orientation == 8:
                            img = img.rotate(90, expand=True)
                except (AttributeError, KeyError, IndexError):
                    # prípad, keď obrázok nemá EXIF informácie
                    pass

                file_size = self.image.size
                print("Before saving image:", img.width, img.height, file_size / (1024 * 1024), "MB")
                
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
                
                print("After saving image:", img.width, img.height, self.image.size / (1024 * 1024), "MB")

                if self.image_thumbnail:
                    if self.image_thumbnail.name != f"{self.image.name.split('.')[0]}_thumbnail.png":
                        img.thumbnail((600, 600), Image.LANCZOS)
                        thumbnail_buffer = BytesIO()
                        img.save(thumbnail_buffer, format='PNG')
                        self.image_thumbnail.save(f"{self.image.name.split('.')[0]}_thumbnail.png", ContentFile(thumbnail_buffer.getvalue()), save=False)
                        print("After saving image thumbnail:", self.image_thumbnail.width, self.image_thumbnail.height, self.image_thumbnail.size / (1024 * 1024), "MB")
                else:
                    img.thumbnail((600, 600), Image.LANCZOS)
                    thumbnail_buffer = BytesIO()
                    img.save(thumbnail_buffer, format='PNG')
                    self.image_thumbnail.save(f"{self.image.name.split('.')[0]}_thumbnail.png", ContentFile(thumbnail_buffer.getvalue()), save=False)
                    print("After saving image thumbnail:", self.image_thumbnail.width, self.image_thumbnail.height, self.image_thumbnail.size / (1024 * 1024), "MB")

        # Save the product instance to create a file path for the video
        try:
            super().save(*args, **kwargs)
        except Exception as e:
            raise ValueError(f"Error saving product: {str(e)}")

        # Spracovanie videa
        if self.video:
            video_path = self.video.path
            base_name, ext = os.path.splitext(os.path.basename(video_path))

            if '_compressed' not in base_name:
                webm_compressed_video_path = os.path.join(os.path.dirname(video_path), f"{base_name}_compressed.webm")
                thumbnail_video_path = os.path.join(os.path.dirname(video_path), f"{base_name}_thumbnail{ext}")

                original_size_mb = os.path.getsize(video_path) / (1024 * 1024)

                if os.path.getsize(video_path) > 2 * 1024 * 1024:  # 2 MB
                    self.compress_video_webm(video_path, webm_compressed_video_path)
                    with open(webm_compressed_video_path, 'rb') as f:
                        self.video_webm = ContentFile(f.read(), name=f"{base_name}_compressed.webm")
                else:
                    with open(video_path, 'rb') as f:
                        self.video_webm = ContentFile(f.read(), name=f"{base_name}_compressed.webm")

                compressed_size_mb = self.video_webm.size / (1024 * 1024)

                if not self.video_thumbnail or self.video_thumbnail.name != f"{base_name}_thumbnail{ext}":
                    self.create_thumbnail(video_path, thumbnail_video_path)
                    original_thumbnail_size_mb = os.path.getsize(thumbnail_video_path) / (1024 * 1024)

                    with open(thumbnail_video_path, 'rb') as f:
                        new_thumbnail_file = ContentFile(f.read(), name=f"{base_name}_thumbnail{ext}")
                    self.video_thumbnail.save(f"{base_name}_thumbnail{ext}", new_thumbnail_file, save=False)

                    compressed_thumbnail_size_mb = self.video_thumbnail.size / (1024 * 1024)

                # Odstránenie dočasných súborov
                for path in [webm_compressed_video_path, thumbnail_video_path]:
                    if os.path.exists(path):
                        os.remove(path)

                print(f"Pred uložením video veľkosť: {original_size_mb:.2f} MB")
                print(f"Po uložení video veľkosť: {compressed_size_mb:.2f} MB")
                print(f"Pred uložením thumbnail veľkosť: {original_thumbnail_size_mb:.2f} MB")
                print(f"Po uložení thumbnail veľkosť: {compressed_thumbnail_size_mb:.2f} MB")

        if not self.image:
            self.image_thumbnail = None
        if not self.video:
            self.video_thumbnail = None

        # Final save to ensure all changes are committed
        try:
            super().save(*args, **kwargs)
        except Exception as e:
            raise ValueError(f"Error saving product after processing: {str(e)}")



    def compress_video_webm(self, input_path, output_path):
        command = [
            'ffmpeg',
            '-y',
            '-i', input_path,
            '-vf', 'scale=1280:-1',
            '-c:v', 'libvpx-vp9',
            '-b:v', '1M',
            '-c:a', 'libopus',
            output_path
        ]

        progress = FfmpegProgress(command)
        try:
            for progress_info in progress.run_command_with_progress():
                logger.info(f"Setting cache with progress: {progress_info}")
                cache.set('video_progress', progress_info, timeout=60)
                print(f"Progress: {progress_info}%")
        except Exception as e:
            logger.error(f"Error during video compression: {str(e)}")
        finally:
            # Vymazanie cache po dokončení alebo prerušení
            logger.info("Clearing cache after process completion")
            cache.delete('video_progress')
            print("Cache cleared after process completion or interruption.")

    def create_thumbnail(self, input_path, output_path):
        command =[
            'ffmpeg',
            '-y',
            '-i', input_path,
            '-ss', '00:00:01.00',
            '-t', '6',
            '-vf', 'scale=640:-2',
            '-b:v', '1050k',
            output_path
        ]

        progress = FfmpegProgress(command)
        try:
            for progress_info in progress.run_command_with_progress():
                cache.set('video_progress', progress_info, timeout=60)
                print(f"Progress: {progress_info}%")
        finally:
            # Vymazanie cache po dokončení alebo prerušení
            cache.delete('video_progress')
            print("Cache cleared after process completion or interruption.")

    def get_meta_description(self):
        return f"Vyrobila som {self.name}. {self.description[:150]}..."




@receiver(pre_save, sender=Product)
def update_product_images(sender, instance, **kwargs):
    if not instance.image:
        instance.image_thumbnail = None







