
from django.contrib import admin

from . import models
from .models import Category
# Register your models here.
@admin.register(Category)
class CateroryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}