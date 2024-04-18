
from django.contrib import admin

from . import models
from .models import Category, Product
# Register your models here.

@admin.register(Category)
class CateroryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category', 'slug', 'image', 'created', 'updated']
    # list_filter = ['in_stock', 'is_active']
    # list_editable = ['price', 'in_stock', 'is_active']
    prepopulated_fields = {'slug': ('name',)}