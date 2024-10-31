
from django.contrib import admin

from . import models
from . import forms
from .models import Category, Product, Blog, BlogImage
# Register your models here.

@admin.register(Category)
class CateroryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','available','category', 'image', 'created', 'updated']
    # list_filter = ['in_stock', 'is_active']
    list_editable = ['available','category']
    prepopulated_fields = {'slug': ('name',)}


class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1  # Počet prázdnych polí pre nahrávanie obrázkov

class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created', 'updated', 'available')
    list_filter = ('available', 'created', 'updated')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [BlogImageInline]
    form = forms.BlogForm  # Priradíme vlastný formulár pre model Blog

admin.site.register(Blog, BlogAdmin)