from django.utils.text import slugify
from django import forms
from django.forms import ImageField
from django.contrib.auth.forms import AuthenticationForm
from .models import Product, Category, Blog, BlogImage

import random

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'image']
        widgets = {
            'slug': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'placeholder': 'Zadaj názov kategórie'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'slug' in self.fields:
            self.fields['slug'].widget.attrs['readonly'] = True
            self.fields['slug'].required = False

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if not slug:  # Ak nie je vyplnený vlastný slug, vyplníme ho na základe názvu
            name = self.cleaned_data['name']
            slug = slugify(name)
            self.instance.slug = slug  # Nastavíme slug instancie Product
        if self.instance.pk:  # Ak je to editácia existujúceho produktu, kontrolujeme unikátnosť slugu
            if Category.objects.filter(slug=slug).exclude(pk=self.instance.pk).exists():
                slug += f'{random.randint(1, 100)}'  # Priradenie náhodného čísla od 1 do 100, ak je slug zhodný
        else:  # Ak je to vytváranie nového produktu, kontrolujeme unikátnosť slugu
            while Category.objects.filter(slug=slug).exists():  # Kontrola, či slug ešte neexistuje
                slug += f'{random.randint(1, 100)}'  # Priradenie náhodného čísla od 1 do 100, ak je slug zhodný
        return slug



# class CustomFileInput(forms.FileInput):
#     def __init__(self, attrs=None, **kwargs):
#         super().__init__(attrs, **kwargs)
#         self.attrs['type'] = 'file'  # Add a custom class for CSS targeting




class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'slug', 'image', 'video', 'category', 'description', 'available']
        widgets = {
            'slug': forms.HiddenInput(),
            # 'image': forms.HiddenInput(),
            # 'image': CustomFileInput(),
            'name': forms.TextInput(attrs={
                # 'class': "form-control-name",
                # 'style': 'max-width: 100px;',
                'placeholder': 'Názov produktu'
                }),
            # 'available': forms.CheckboxInput(attrs={
            #     'class': "form-control-input",
            #     # 'style': 'min-width: 100px;',
            #     # 'placeholder': 'Name'
            #     }),

            # 'image': forms.FileInput(attrs={
            #     # 'class': "form-control-input",
            #     # 'style': 'max-width: 100px;',
            #     'placeholder': 'Obrazok',
            #     'label': 'Vybrať súbor',
            #     }),

                
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'slug' in self.fields:
            self.fields['slug'].widget.attrs['readonly'] = True
            self.fields['slug'].required = False

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if not slug:  # Ak nie je vyplnený vlastný slug, vyplníme ho na základe názvu
            name = self.cleaned_data['name']
            slug = slugify(name)
            self.instance.slug = slug  # Nastavíme slug instancie Product
        if self.instance.pk:  # Ak je to editácia existujúceho produktu, kontrolujeme unikátnosť slugu
            if Product.objects.filter(slug=slug).exclude(pk=self.instance.pk).exists():
                slug += f'{random.randint(1, 100)}'  # Priradenie náhodného čísla od 1 do 100, ak je slug zhodný
        else:  # Ak je to vytváranie nového produktu, kontrolujeme unikátnosť slugu
            while Product.objects.filter(slug=slug).exists():  # Kontrola, či slug ešte neexistuje
                slug += f'{random.randint(1, 100)}'  # Priradenie náhodného čísla od 1 do 100, ak je slug zhodný
        return slug

    def clean(self):
        cleaned_data = super().clean()
        if 'image' in self.changed_data and not cleaned_data.get('image'):
            cleaned_data['image_thumbnail'] = None
        return cleaned_data



class BlogImageForm(forms.ModelForm):
    class Meta:
        model = BlogImage
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Vyber fotku'
            })
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'slug', 'description', 'available']
        widgets = {
            'slug': forms.HiddenInput(),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Názov článku'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Obsah článku'
            }),
            'available': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'slug' in self.fields:
            self.fields['slug'].widget.attrs['readonly'] = True
            self.fields['slug'].required = False

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if not slug:
            name = self.cleaned_data['name']
            slug = slugify(name)
            self.instance.slug = slug
        if self.instance.pk:
            if Blog.objects.filter(slug=slug).exclude(pk=self.instance.pk).exists():
                slug += f'{random.randint(1, 100)}'
        else:
            while Blog.objects.filter(slug=slug).exists():
                slug += f'{random.randint(1, 100)}'
        return slug

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Meno'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Heslo'}))
