from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.forms import modelformset_factory
from .models import Category ,Product, Blog, BlogImage
from .forms import ProductForm, CategoryForm, BlogForm, BlogImageForm
from django.http import JsonResponse
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.

def home(request):

    products = Product.objects.filter(available=True).order_by('-created')[:10]
    context = {

        'products': products,
    
    }

    return render(request, 'home.html', context)


def about_me(request):

    products = Product.objects.filter(available=True).order_by('-created')[:10]
    context = {

        'products': products,
    
    }

    return render(request, 'about_me.html', context)

def blog_view(request):
    blogs = Blog.objects.filter(available=True).order_by('-created')[:10]
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog.html', context)

# @login_required
# def add_blog(request):
#     ImageFormSet = modelformset_factory(BlogImage, form=BlogImageForm, extra=3)  # Adjust 'extra' to allow multiple images
#     if request.method == 'POST':
#         form = BlogForm(request.POST)
#         formset = ImageFormSet(request.POST, request.FILES, queryset=BlogImage.objects.none())
        
#         if form.is_valid() and formset.is_valid():
#             blog = form.save(commit=False)
#             blog.save()

#             for form in formset.cleaned_data:
#                 if form:
#                     image = form['image']
#                     photo = BlogImage(blog=blog, image=image)
#                     photo.save()
                    
#             return redirect('blog')
#     else:
#         form = BlogForm()
#         formset = ImageFormSet(queryset=BlogImage.objects.none())
    
#     return render(request, 'add_blog.html', {'form': form, 'image_forms': formset})


@login_required
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        image_forms = [BlogImageForm(request.POST, request.FILES, prefix=str(i)) for i in range(5)]

        if form.is_valid() and all([img_form.is_valid() for img_form in image_forms]):
            valid = True
            for img_form in image_forms:
                image_file = img_form.cleaned_data.get('image')
                if image_file and image_file.size > 15 * 1024 * 1024:  # 15 MB size limit
                    img_form.add_error('image', "The image size must be less than 15 MB.")
                    valid = False

            if valid:
                blog = form.save()
                for img_form in image_forms:
                    if img_form.cleaned_data.get('image'):
                        image = img_form.save(commit=False)
                        image.blog = blog
                        image.save()
                return redirect('/blog')  # Redirect to the blog list page

    else:
        form = BlogForm()
        image_forms = [BlogImageForm(prefix=str(i)) for i in range(5)]

    context = {
        'form': form,
        'image_forms': image_forms
    }
    return render(request, 'add_blog.html', context)


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import BlogForm, BlogImageForm
from .models import Blog, BlogImage

@login_required
def update_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    
    # Retrieve existing images for this blog
    existing_images = blog.images.all()
    num_existing_images = existing_images.count()
    
    max_images = 5
    num_new_image_forms = max_images - num_existing_images
    
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        image_forms = [BlogImageForm(request.POST, request.FILES, prefix=str(i)) for i in range(num_new_image_forms)]
        
        valid = True  # Flag to check overall validity
        
        # Validate existing image replacements
        for image in existing_images:
            replacement_file = request.FILES.get(f'replace_image_{image.id}')
            if replacement_file and replacement_file.size > 15 * 1024 * 1024:  # 15 MB size limit
                form.add_error(None, f"The image size must be less than 15 MB.")
                valid = False
        
        # Validate new image uploads
        if form.is_valid() and all([img_form.is_valid() for img_form in image_forms]):
            for img_form in image_forms:
                image_file = img_form.cleaned_data.get('image')
                if image_file and image_file.size > 15 * 1024 * 1024:  # 15 MB size limit
                    img_form.add_error('image', "The image size must be less than 15 MB.")
                    valid = False
            
            if valid:
                blog = form.save()

                # Handle image replacements and deletions
                for image in existing_images:
                    if request.POST.get(f'delete_image_{image.id}'):
                        image.delete()
                    elif request.FILES.get(f'replace_image_{image.id}'):
                        image.image = request.FILES.get(f'replace_image_{image.id}')
                        image.save()

                # Handle new image uploads
                for img_form in image_forms:
                    if img_form.cleaned_data.get('image'):
                        new_image = img_form.save(commit=False)
                        new_image.blog = blog
                        new_image.save()

                return redirect('/blog')  # Redirect to the blog list page
    else:
        form = BlogForm(instance=blog)
        image_forms = [BlogImageForm(prefix=str(i)) for i in range(num_new_image_forms)]

    context = {
        'form': form,
        'image_forms': image_forms,
        'existing_images': existing_images,
        'blog': blog,  # Ensure blog is passed to the template
    }
    return render(request, 'update_blog.html', context)







@login_required
def delete_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == 'POST':
        blog.delete()
        return redirect('/blog')  # Presmerovanie na stránku s úspechom
    return render(request, 'delete_blog.html', {'blog': blog})


def contact(request):

    products = Product.objects.filter(available=True).order_by('-created')[:5]
    context = {

        'products': products,
    
    }

    return render(request, 'contact.html', context)




def gallery(request):
    category_slug = request.GET.get('category', '')
    page_number = request.GET.get('page', 1)
    
    # Získanie uloženej hodnoty počtu položiek na stránku z session, alebo použitie defaultnej hodnoty (15)
    items_per_page = request.session.get('items_per_page', 15)

    if category_slug:
        if request.user.is_authenticated:
            products = Product.objects.filter(category__slug=category_slug)
        else:
            products = Product.objects.filter(category__slug=category_slug, available=True)
    else:
        if request.user.is_authenticated:
            products = Product.objects.all()
        else:
            products = Product.objects.filter(available=True)

    paginator = Paginator(products, items_per_page)
    page_obj = paginator.get_page(page_number)

    # Vypočítať rozsah stránok
    current_page = page_obj.number
    total_pages = paginator.num_pages
    first_range = []
    middle_range = []
    last_range = []

    if total_pages <= 7:
        first_range = range(1, total_pages + 1)
    elif current_page <= 4:
        first_range = range(1, 6)
        last_range = range(total_pages - 1, total_pages + 1)
    elif current_page >= total_pages - 3:
        first_range = range(1, 3)
        last_range = range(total_pages - 4, total_pages + 1)
    else:
        first_range = range(1, 3)
        middle_range = range(current_page - 1, current_page + 2)
        last_range = range(total_pages - 1, total_pages + 1)

    # Pridanie kontextu
    context = {
        'products': page_obj,
        'categories': Category.objects.all(),
        'selected_category': category_slug,
        'first_range': first_range,
        'middle_range': middle_range,
        'last_range': last_range,
        'paginator': paginator,  # Pridáme paginator do kontextu
        # 'show_footer': True, 
    }

    # Uloženie vybranej hodnoty počtu položiek na stránku do session
    if 'itemsPerPage' in request.GET:
        items_per_page = int(request.GET['itemsPerPage'])
        request.session['items_per_page'] = items_per_page
        return redirect(request.path)

    # Skontrolujte, či je požiadavka AJAX
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Ak je to AJAX, vráťte iba čiastočnú šablónu
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
            if image_file and image_file.size > 15 * 1024 * 1024:  
                form.add_error('image', "The image size must be less than 15 MB.")
            else:
                video_file = request.FILES.get('video')
                if video_file and video_file.size > 120 * 1024 * 1024: 
                    form.add_error('video', "The video size must be less than 120 MB.")
                else:
                    form.save()
                    return redirect('gallery')
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form, 'product': product})

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
        # 'show_footer': True, 
    }
    return render(request, 'product_detail.html', context)

def BlogDetailView(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    context = {
        'blog': blog,
        # 'show_footer': True, 
    }
    return render(request, 'blog_detail.html', context)

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
