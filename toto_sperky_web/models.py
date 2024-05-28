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
from PIL import Image
from io import BytesIO
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(blank=True, null=True,)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(blank=True, null=True)
    video = models.FileField(blank=True, null=True)  # Nové pole pre video súbor
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('toto_sperky_web:product_detail', args=[self.slug])

    class Meta:
        verbose_name_plural = 'products'
        ordering = ('-created',)

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     print("Before saving:", self.image.width, self.image.height, self.image.size / (1024 * 1024), "MB")
    #     print("Before saving video:",  self.video.size / (1024 * 1024), "MB")
        
    #     if self.video:
    #         try:
    #             # Uloženie originálneho videa
    #             super().save(*args, **kwargs)
                
    #             # Zmena veľkosti videa
    #             video_clip = VideoFileClip(self.video.path)
    #             resized_clip = video_clip.resize(0.5)  # Zmeňte na vašu preferovanú úroveň zmeny veľkosti
                
    #             # Uloženie zmenšeného videa do dočasného súboru
    #             with tempfile.NamedTemporaryFile(suffix='.mp4', delete=False) as temp_video:
    #                 resized_clip.write_videofile(temp_video.name, codec="libx264", audio_codec="aac", remove_temp=True)
                    
    #                 # Vytvoriť InMemoryUploadedFile z dočasného súboru a uložiť do modelu
    #                 self.video.save('resized_' + os.path.basename(self.video.name), InMemoryUploadedFile(temp_video, None, 'resized_' + os.path.basename(self.video.name), 'video/mp4', os.path.getsize(temp_video.name), None))
                    
    #             # Vymazať originálne video
    #             os.remove(self.video.path)
    #             self.video.name = 'resized_' + os.path.basename(self.video.name)
    #         except Exception as e:
    #             print("An error occurred during video resizing:", e)
    #             # Ak nastane chyba, zachovajte originálny súbor videa

    #     if self.image:
    #         # Získanie veľkosti súboru v bajtoch
    #         file_size = self.image.size
            
    #         # Podmienka pre veľkosť súboru 8MB
    #         if file_size > 2 * 1024 * 1024:  # 8MB prevedené na bajty
    #             img = Image.open(self.image)
        
    #             # Zmenšiť obrázok na tretinu a znížiť kvalitu
    #             img.thumbnail((img.width / 3, img.height / 3), Image.LANCZOS)
    #             buffer = BytesIO()
    #             img.save(buffer, format='JPEG', quality=60)
    #             self.image = InMemoryUploadedFile(buffer, None, f"{self.image.name.split('.')[0]}_compressed.jpg", 'image/jpeg', buffer.tell(), None)
                
    #     print("After saving:", self.image.width, self.image.height, self.image.size / (1024 * 1024), "MB")
    #     print("After saving video:",  self.video.size / (1024 * 1024), "MB")
        
        super().save(*args, **kwargs)





    def save(self, *args, **kwargs):
        print("Before saving:", self.image.width, self.image.height, self.image.size / (1024 * 1024), "MB")
        print("Before saving video:",  self.video.size / (1024 * 1024), "MB")
        if self.video:
            # Uloženie originálneho videa
            super().save(*args, **kwargs)
            
            # Zmena veľkosti videa
            video_clip = VideoFileClip(self.video.path)
            resized_clip = video_clip.resize(0.5)  # Zmeňte na vašu preferovanú úroveň zmeny veľkosti
            resized_video_path = os.path.join(os.path.dirname(self.video.path), 'resized_' + os.path.basename(self.video.path))
            resized_clip.write_videofile(resized_video_path, codec="libx264", audio_codec="aac", remove_temp=True)
            
           
            os.remove(self.video.path)

            self.video.name = 'resized_' + os.path.basename(self.video.name)

        if self.image:
            # Získanie veľkosti súboru v bajtoch
            file_size = self.image.size
            
            # Podmienka pre veľkosť súboru 8MB
            if file_size > 2 * 1024 * 1024:  # 8MB prevedené na bajty
                img = Image.open(self.image)
        
                # Zmenšiť obrázok na tretinu a znížiť kvalitu
                img.thumbnail((img.width / 3, img.height / 3), Image.LANCZOS)
                buffer = BytesIO()
                img.save(buffer, format='JPEG', quality=60)
                self.image = InMemoryUploadedFile(buffer, None, f"{self.image.name.split('.')[0]}_compressed.jpg", 'image/jpeg', buffer.tell(), None)
        print("After saving:", self.image.width, self.image.height, self.image.size / (1024 * 1024), "MB")
        print("After saving video:",  self.video.size / (1024 * 1024), "MB")
        super().save(*args, **kwargs)