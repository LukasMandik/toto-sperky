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



