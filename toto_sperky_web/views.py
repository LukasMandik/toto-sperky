from django.shortcuts import render
from django.http import HttpResponse
from .models import Category ,Product
# Create your views here.


def home(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    context = {
        'categories': categories,
        'products': products,
    
    }

    return render(request, 'home.html', context)


def gallery(request):
    category_name = request.GET.get('category', '')
    categories = Category.objects.all()


    if category_name:
        products = Product.objects.filter(category__name=category_name).order_by('-id')
    else:
        products = Product.objects.all().order_by('-id')



    # products = Product.objects.filter(available=True)  # Assuming 'available' field for product availability

 

    context = {
        'categories': categories,
        'products': products,
        'selected_category': category_name,
    }
    return render(request, 'gallery.html', context)



def cookies(request):

    return render(request, 'cookies.html')