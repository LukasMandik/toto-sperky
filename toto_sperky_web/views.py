from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Category ,Product
from .forms import ProductForm, CategoryForm
from django.http import JsonResponse
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):

    products = Product.objects.filter(available=True).order_by('-created')[:5]
    context = {

        'products': products,
    
    }

    return render(request, 'home.html', context)


def about_me(request):

    products = Product.objects.filter(available=True).order_by('-created')[:5]
    context = {

        'products': products,
    
    }

    return render(request, 'about_me.html', context)

def gallery(request):
    category_name = request.GET.get('category', '')
    products = Product.objects.filter(category__name=category_name) if category_name else Product.objects.all()

    context = {
        'products': products,
        'categories': Category.objects.all(),
        'selected_category': category_name,
    }

    # Skontrolujte, či je požiadavka AJAX
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Ak je to AJAX, vráťte iba partial
        return render(request, 'partials/product_list.html', context)

    # Inak vráťte celú šablónu
    return render(request, 'gallery.html', context)

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES.get('image')
            if image_file and image_file.size > 15 * 1024 * 1024:  # Veľkosť v bajtoch, 15 MB = 15 * 1024 * 1024 bajtov
                form.add_error('image', "The image size must be less than 15 MB.")
            else:
                video_file = request.FILES.get('video')
                if video_file and video_file.size > 120 * 1024 * 1024:  # Veľkosť v bajtoch, 120 MB = 120 * 1024 * 1024 bajtov
                    form.add_error('video', "The video size must be less than 120 MB.")
                else:
                    form.save()
                    return redirect('gallery')  # Přesměrování na stránku s úspěchem
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES.get('image')
            if image_file and image_file.size > 15 * 1024 * 1024:  # Veľkosť v bajtoch, 15 MB = 15 * 1024 * 1024 bajtov
                form.add_error('image', "The image size must be less than 15 MB.")
            else:
                form.save()
                return redirect('gallery')  # Přesměrování na stránku s úspěchem
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})


@login_required
def update_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            image_file = request.FILES.get('image')
            if image_file and image_file.size > 15 * 1024 * 1024:  # Veľkosť v bajtoch, 15 MB = 15 * 1024 * 1024 bajtov
                form.add_error('image', "The image size must be less than 15 MB.")
            else:
                video_file = request.FILES.get('video')
                if video_file and video_file.size > 120 * 1024 * 1024:  # Veľkosť v bajtoch, 120 MB = 120 * 1024 * 1024 bajtov
                    form.add_error('video', "The video size must be less than 120 MB.")
                else:
                    form.save()
                    return redirect('gallery')  # Presmerovanie na stránku s úspechom
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form})

@login_required
def update_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            image_file = request.FILES.get('image')
            if image_file and image_file.size > 15 * 1024 * 1024:  # Veľkosť v bajtoch, 15 MB = 15 * 1024 * 1024 bajtov
                form.add_error('image', "The image size must be less than 15 MB.")
            else:
            
                form.save()
                return redirect('gallery')  # Presmerovanie na stránku s úspechom
    else:
        form = CategoryForm(instance=category)
    return render(request, 'update_category.html', {'form': form, 'category': category})


@login_required
def delete_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        product.delete()
        return redirect('gallery')  # Presmerovanie na stránku s úspechom
    return render(request, 'delete_product.html', {'product': product})

@login_required
def delete_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        category.delete()
        return redirect('gallery')  # Presmerovanie na stránku s úspechom
    return render(request, 'delete_category.html', {'category': category})


def ProductDetailView(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product,
        'show_footer': True, 
    }
    return render(request, 'product_detail.html', context)

@login_required
def product_data(request, slug):
    product = get_object_or_404(Product, slug=slug)
    data = {
        'name': product.name,
        'description': product.description,
        'image_url': product.image.url,
    }
    return JsonResponse(data)


def cookies(request):

    return render(request, 'cookies.html')

def search_results(request):
    query = request.GET.get('q', '')  # Získať hľadaný výraz
    
    # Vyhľadajte podľa rôznych kritérií
    results = []
    
    # Hľadanie podľa názvu
    products_by_name = Product.objects.filter(name__icontains=query)
    for product in products_by_name:
        product.search_type = 'Názvu'  # Označiť spôsob nájdenia
        results.append(product)

    # Hľadanie podľa popisu
    products_by_description = Product.objects.filter(description__icontains=query)
    for product in products_by_description:
        if product not in results:  # Pridať iba vtedy, ak ešte nie je v výsledkoch
            product.search_type = 'Popisu'
            results.append(product)

    # Hľadanie podľa kategórie
    products_by_category = Product.objects.filter(category__name__icontains=query)
    for product in products_by_category:
        if product not in results:
            product.search_type = 'Kategorie'
            results.append(product)

    context = {
        'query': query,
        'results': results,
    }

    return render(request, 'search_results.html', context)
