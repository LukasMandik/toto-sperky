from django.urls import path

from .views import home, gallery, ProductDetailView, cookies, product_data, about_me, contact, blog_view, BlogDetailView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name = 'toto_sperky_web'

urlpatterns = [
    path('', home, name='home'),
    # path('search/', search_results, name='search_results'),
    path('gallery/', gallery, name='gallery'),
    path('blog/', blog_view, name='blog'),
    path('about_me/', about_me, name='about_me'),
    path('contact/', contact, name='contact'),
    # path('<slug:category_slug>/', views.gallery, name='product_gallery_by_category'),
    path('product/<slug:slug>/', ProductDetailView, name='product_detail'),
    path('blog/<slug:slug>/', BlogDetailView, name='blog_detail'),
    path('cookies/', cookies, name='cookies'),
    path('product/<slug:slug>/data/', product_data, name='product_data'),
    # path('add_product/', add_product, name='add_product'),
    # path('product/<slug:slug>/update/', update_product, name='update_product'),
    # path('product/<slug:slug>/delete/', delete_product, name='delete_product'),
]

urlpatterns += staticfiles_urlpatterns()