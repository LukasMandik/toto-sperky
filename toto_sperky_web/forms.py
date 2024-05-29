from django import forms
from .models import Product
from django.utils.text import slugify

from django import forms
from .models import Product
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'slug', 'image', 'video', 'category', 'description', 'available']
        widgets = {
            'slug': forms.HiddenInput(),  # Skryje pole slug
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'slug' in self.fields:  # Kontrola existence pole slug v polích formuláře
            self.fields['slug'].widget.attrs['readonly'] = True  # Pole slug bude pouze pro čtení
            self.fields['slug'].required = False  # Pole slug nebude povinné

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('slug') and cleaned_data.get('name'):
            cleaned_data['slug'] = slugify(cleaned_data['name'])  # Automaticky vyplní pole slug na základě pole name
        return cleaned_data