from django.db import models
from django.urls import reverse
from django.urls import reverse
from PIL import Image
import os
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
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
    image = models.ImageField(blank=True, null=True,)
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
        print("Before saving:", self.image.width, self.image.height, self.image.size )
        if self.image:
            # Získanie veľkosti súboru v bajtoch
            file_size = self.image.size
            
            # Podmienka pre veľkosť súboru 8MB
            if file_size > 2 * 1024 * 1024:  # 8MB prevedené na bajty
                img = Image.open(self.image)
        
                # Zmenšiť obrázok na tretinu a znížiť kvalitu
                img.thumbnail((img.width / 3, img.height / 3))
                buffer = BytesIO()
                img.save(buffer, format='JPEG', quality=60)
                self.image = InMemoryUploadedFile(buffer, None, f"{self.image.name.split('.')[0]}_compressed.jpg", 'image/jpeg', buffer.tell(), None)
        
        print("After saving:", self.image.width, self.image.height, self.image.size )
        super().save(*args, **kwargs)
