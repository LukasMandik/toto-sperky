from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category ,Product
from django.http import JsonResponse
# Create your views here.


def home(request):

    products = Product.objects.filter(available=True).order_by('-created')[:5]
    context = {

        'products': products,
    
    }

    return render(request, 'home.html', context)


def gallery(request):
    category_name = request.GET.get('category', '')
    product_slug = request.GET.get('product', '')  # Získa slug produktu z URL
    categories = Category.objects.all()

    if category_name:
        products = Product.objects.filter(category__name=category_name).order_by('-created')
    else:
        products = Product.objects.all().order_by('-created')

    context = {
        'categories': categories,
        'products': products,
        'selected_category': category_name,
    }

    # Ak je zadaný product_slug, načítajte a pridajte produkt do kontextu
    if product_slug:
        selected_product = get_object_or_404(Product, slug=product_slug)
        context['selected_product'] = selected_product  # Pridajte do kontextu pre modálne zobrazenie
    
    return render(request, 'gallery.html', context)



def ProductDetailView(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product,
    }
    return render(request, 'product_detail.html', context)


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