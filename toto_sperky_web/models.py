from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    # def get_absolute_url(self):
    #     return reverse('photos_web:category_list', args=[self.slug])

    def __str__(self):
        return self.name
