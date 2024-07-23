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

        # Zpracování videa
        if self.video:
            super().save(*args, **kwargs)
            print("Before saving video:", self.video.size / (1024 * 1024), "MB")
            
            # Spracovanie hlavného videa
            cap = cv2.VideoCapture(self.video.path)
            fourcc = cv2.VideoWriter_fourcc(*'avc1')

            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            print("Original video dimensions:", width, "x", height)

            max_side_length = 1800
            if width > height:
                new_width = max_side_length
                new_height = int(height * (max_side_length / width))
            else:
                new_height = max_side_length
                new_width = int(width * (max_side_length / height))

            dim = (new_width, new_height)
            bitrate = 1000000
            framerate = 30.0

            resized_video_path = os.path.join(os.path.dirname(self.video.path), 'resized_' + os.path.basename(self.video.path))
            out = cv2.VideoWriter(resized_video_path, fourcc, framerate, dim, isColor=True)
            out.set(cv2.CAP_PROP_BITRATE, bitrate)

            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            prev_frame = None
            processed_frames = 0

            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                resized_frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
                if prev_frame is not None:
                    resized_frame = cv2.addWeighted(resized_frame, 0.5, prev_frame, 0.5, 0)
                out.write(resized_frame)
                prev_frame = resized_frame

                processed_frames += 1
                progress = (processed_frames / total_frames) * 100
                sys.stdout.write(f"\rProgress: {progress:.2f}%")
                sys.stdout.flush()

            cap.release()
            out.release()
            os.remove(self.video.path)
            self.video.name = 'resized_' + os.path.basename(self.video.name)
            print("Resized video dimensions:", new_width, "x", new_height)
            print("After saving video:", os.path.getsize(resized_video_path) / (1024 * 1024), "MB")

            # Spracovanie náhľadu videa
            cap = cv2.VideoCapture(resized_video_path)
            fourcc = cv2.VideoWriter_fourcc(*'avc1')

            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            print("Original video dimensions for thumbnail:", width, "x", height)

            max_side_length = 600
            if width > height:
                new_width = max_side_length
                new_height = int(height * (max_side_length / width))
            else:
                new_height = max_side_length
                new_width = int(width * (max_side_length / height))

            dim = (new_width, new_height)
            bitrate = 1000000
            framerate = 30.0

            thumbnail_video_path = os.path.join(os.path.dirname(self.video.path), 'thumbnail_' + os.path.basename(self.video.path))
            out = cv2.VideoWriter(thumbnail_video_path, fourcc, framerate, dim, isColor=True)
            out.set(cv2.CAP_PROP_BITRATE, bitrate)

            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            prev_frame = None
            processed_frames = 0

            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                resized_frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
                if prev_frame is not None:
                    resized_frame = cv2.addWeighted(resized_frame, 0.5, prev_frame, 0.5, 0)
                out.write(resized_frame)
                prev_frame = resized_frame

                processed_frames += 1
                progress = (processed_frames / total_frames) * 100
                sys.stdout.write(f"\rProgress: {progress:.2f}%")
                sys.stdout.flush()

            cap.release()
            out.release()

            # Uloženie názvu náhľadu videa
            self.video_thumbnail.name = 'thumbnail_' + os.path.basename(self.video.name)
            print("Resized video dimensions for thumbnail:", new_width, "x", new_height)
            print("After saving video thumbnail:", os.path.getsize(thumbnail_video_path) / (1024 * 1024), "MB")






        # Zpracování obrázku
        if self.image:
            # Vytvoření náhledového obrázku
            with Image.open(self.image) as img:
                # Získanie veľkosti súboru v bajtoch
                file_size = self.image.size
                print("Before saving image:", self.image.width, self.image.height, self.image.size / (1024 * 1024), "MB")
                if file_size > 2 * 1024 * 1024:  # 2 MB prevedené na bajty
                        # Získání původních rozměrů obrázku
                        orig_width, orig_height = img.size
                        # Zjistit orientaci obrazku
                        if orig_width > orig_height:
                            # Zmenit velikost na max. 1200x...
                            new_width = 1200
                            new_height = int((orig_height / orig_width) * new_width)
                        else:
                            # Zmenit velikost na max. ...x1200
                            new_height = 1200
                            new_width = int((orig_width / orig_height) * new_height)
                        img.thumbnail((new_width, new_height), Image.LANCZOS)
                        buffer = BytesIO()
                        img.save(buffer, format='PNG')
                        self.image = InMemoryUploadedFile(buffer, None, f"{self.image.name.split('.')[0]}_compressed.png", 'image/png', buffer.tell(), None)
                print("After saving image:", self.image.width, self.image.height, self.image.size / (1024 * 1024), "MB")
                if self.image_thumbnail:
                    # file_size_thumb = self.image_thumbnail.size
                    # if file_size_thumb > 0.1 * 1024 * 1024:   
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



@receiver(pre_save, sender=Product)
def update_product_images(sender, instance, **kwargs):
    if not instance.image:
        instance.image_thumbnail = None


# @receiver(pre_delete, sender=Product)
# def delete_product_images(sender, instance, **kwargs):
#     # Získajte príslušné fotografie spojené s produktom a vymažte ich
#     if instance.image:
#         instance.image.delete()
#     if instance.image_thumbnail:
#         instance.image_thumbnail.delete()
#     if instance.video:
#         instance.video.delete()
#     if instance.video_thumbnail:
#         instance.video_thumbnail.delete()
# @receiver(pre_save, sender=Product)
# def update_product_images(sender, instance, **kwargs):
#     # Skontrolujte, či sa zmenila fotka a ak áno, odstráňte starú a vytvorte novú
#     if instance.pk:
#         try:
#             old_instance = Product.objects.get(pk=instance.pk)
#             if old_instance.image != instance.image:
#                 if old_instance.image:
#                     old_instance.image.delete()
#                 if old_instance.image_thumbnail:
#                     old_instance.image_thumbnail.delete()
#         except Product.DoesNotExist:
#             pass

    # Tu pridajte váš kód pre spracovanie nového obrázku
  
        # Vytváranie náhľadového obrá
           
        # if self.image:
        #     print("Before saving image:", self.image.width, self.image.height, self.image.size / (1024 * 1024), "MB")
            
        #     # Získání velikosti souboru v bajtech
        #     file_size = self.image.size
            
        #     # Cílová velikost souboru pro kompresi (v bajtech)
        #     target_size = 3 * 1024 * 1024  # 2 MB
            
        #     # Rozdíl mezi aktuální a cílovou velikostí
        #     size_difference = target_size - file_size
            
        #     # Procentuální změna velikosti
        #     size_change_percentage = size_difference / file_size
            
        #     # Výpočet kvality komprese na základě procentuální změny velikosti
        #     compression_quality = int(100 * (1 + size_change_percentage))
            
        #     # Otevření obrázku
        #     img = Image.open(self.image)
            
        #     # Změna velikosti obrázku (volitelné, upravte podle potřeby)
        #     img.thumbnail((img.width / 3, img.height / 3), Image.LANCZOS)
            
        #     # Uložení obrázku s určitou kvalitou komprese a formátem
        #     buffer = BytesIO()
        #     img.save(buffer, format='PNG', quality=compression_quality)
        #     self.image = InMemoryUploadedFile(buffer, None, f"{self.image.name.split('.')[0]}_compressed.png", 'image/png', buffer.tell(), None)
            
        #     # Výpis detailů komprese pro ladění
        #     print(f"Compression quality: {compression_quality}")
            
        #     print("After saving image:", self.image.width, self.image.height, self.image.size / (1024 * 1024), "MB")
      

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
        
        # super().save(*args, **kwargs)





    # def save(self, *args, **kwargs):
    #     print("Before saving:", self.image.width, self.image.height, self.image.size / (1024 * 1024), "MB")
    #     print("Before saving video:",  self.video.size / (1024 * 1024), "MB")
    #     if self.video:
    #         # Uloženie originálneho videa
    #         super().save(*args, **kwargs)
            
    #         # Zmena veľkosti videa
    #         video_clip = VideoFileClip(self.video.path)
    #         resized_clip = video_clip.resize(0.1)  # Zmeňte na vašu preferovanú úroveň zmeny veľkosti
    #         resized_video_path = os.path.join(os.path.dirname(self.video.path), 'resized_' + os.path.basename(self.video.path))
    #         resized_clip.write_videofile(resized_video_path, codec="libx264", audio_codec="aac", remove_temp=True)
            
           
    #         os.remove(self.video.path)

    #         self.video.name = 'resized_' + os.path.basename(self.video.name)

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
    #     super().save(*args, **kwargs)








