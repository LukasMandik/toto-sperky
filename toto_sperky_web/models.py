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
import cv2
import sys
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
    image = models.ImageField(null=True, blank=True)
    video = models.FileField(null=True,blank=True)   # Nové pole pre video súbor
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

    def save(self, *args, **kwargs):

        if self.video:
            print("Before saving video:", self.video.size / (1024 * 1024), "MB")
            super().save(*args, **kwargs)
            # Open the video file
            cap = cv2.VideoCapture(self.video.path)

            # Define the codec for the output video
            fourcc = cv2.VideoWriter_fourcc(*'avc1')  # Updated codec to 'avc1'

            # Get the frame width and height
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            # Define the desired scale percentage (e.g., 20%)
            scale_percent = 20

            # Calculate the new width and height
            new_width = int(width * scale_percent / 100)
            new_height = int(height * scale_percent / 100)

            # Define the dimensions for the resized video
            dim = (new_width, new_height)

            # Create a VideoWriter object for the resized video
            resized_video_path = os.path.join(os.path.dirname(self.video.path), 'resized_' + os.path.basename(self.video.path))
            out = cv2.VideoWriter(resized_video_path, fourcc, 30.0, dim)

            # Get the total number of frames in the video
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

            # Read and resize each frame, then write it to the resized video
            prev_frame = None
            processed_frames = 0
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                resized_frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
                
                # Apply video stabilization (average neighboring frames)
                if prev_frame is not None:
                    resized_frame = cv2.addWeighted(resized_frame, 0.5, prev_frame, 0.5, 0)
                
                out.write(resized_frame)
                prev_frame = resized_frame
                
                # Increment processed frames count
                processed_frames += 1
                
                # Calculate and display progress
                progress = (processed_frames / total_frames) * 100
                sys.stdout.write(f"\rProgress: {progress:.2f}%")
                sys.stdout.flush()  # Flush the output buffer to ensure immediate display

            # Release the video capture and writer
            cap.release()
            out.release()

            os.remove(self.video.path)
            self.video.name = 'resized_' + os.path.basename(self.video.name)
            print("After saving video:", self.video.size / (1024 * 1024), "MB")

        if self.image:
            print("Before saving image:", self.image.width, self.image.height, self.image.size / (1024 * 1024), "MB")
            # Získání velikosti souboru v bajtech
            file_size = self.image.size

            # Výpočet koeficientu komprese na základě velikosti obrázku
            target_size = 5 * 1024 * 1024  # Maximální cílová velikost 5 MB
            compression_ratio = target_size / file_size
            compression_quality = int(100 / compression_ratio)

            # Otevření obrázku
            img = Image.open(self.image)

            # Úprava velikosti obrázku na třetinu
            # img.thumbnail((img.width / 3, img.height / 3), Image.LANCZOS)

            # Uložení obrázku s danou úrovní komprese
            buffer = BytesIO()
            img.save(buffer, format='JPEG', quality=compression_quality)
            self.image = InMemoryUploadedFile(buffer, None, f"{self.image.name.split('.')[0]}_compressed.jpg", 'image/jpeg', buffer.tell(), None)
            print(f"compression_ratio:{compression_ratio}")
            print("After saving image:", self.image.width, self.image.height, self.image.size / (1024 * 1024), "MB")
        super().save(*args, **kwargs)
      
      

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








