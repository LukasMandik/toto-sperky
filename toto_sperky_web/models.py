from django.db import models
from django.urls import reverse
from django.urls import reverse
from PIL import Image
import os
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





    # def save(self, *args, **kwargs):


       

        # # Convert the image to WebP format
        # width, height = img.size
        # new_size = (width // 7, height // 7)
        # img.thumbnail(new_size)
        #
        # webp_image_path = os.path.splitext(self.image.path)[0] + '.webp'
        # img.save(webp_image_path, 'WEBP', quality=100, lossless=True)
        # self.webp_image.name = os.path.join('photos_web', 'static', 'photos', os.path.basename(webp_image_path))

        # Convert the image to PNG format
        # img = Image.open(self.image.path)

        # width, height = img.size
        # new_size = (width // 7, height // 7)
        # img.thumbnail(new_size)

        # png_image_path = os.path.splitext(self.image.path)[0] + '.png'
        # img.save(png_image_path, 'PNG', compress_level=9)
        # self.png_image.name = os.path.join(os.path.basename(png_image_path))

        # super(Product, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'products'
        ordering = ('-created',)

    # def get_absolute_url(self):
    #     return reverse('toto_sperky_web:product_detail', args=[self.slug])

    def __str__(self):
        return self.name