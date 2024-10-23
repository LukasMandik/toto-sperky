from django.urls import path

from .views import home, gallery, ProductDetailView, cookies, product_data, about_me, contact, blog_view, BlogDetailView, category_detail, UserLoginView, search_results, search_suggestions, add_blog, update_blog, delete_blog, add_product, update_product, delete_product, add_category, update_category, delete_category
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LogoutView

app_name = 'toto_sperky_web'

urlpatterns = [
    path('', home, name='home'),
    path('gallery/', gallery, name='gallery'),
    path('search/', search_results, name='search_results'),
    path('search_suggestions/', search_suggestions, name='search_suggestions'),  # Pridanie tejto línie
    path('add_blog/', add_blog, name='add_blog'),
    path('blog/<slug:slug>/update/', update_blog, name='update_blog'),
    path('blog/<slug:slug>/delete/', delete_blog, name='delete_blog'),
    path('add_product/', add_product, name='add_product'),
    path('product/<slug:slug>/update/', update_product, name='update_product'),
    path('product/<slug:slug>/delete/', delete_product, name='delete_product'),
    path('add_category/', add_category, name='add_category'),
    path('category/<slug:slug>/update/', update_category, name='update_category'),
    path('category/<slug:slug>/delete/', delete_category, name='delete_category'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path('blog/', blog_view, name='blog'),
    path('about_me/', about_me, name='about_me'),
    path('contact/', contact, name='contact'),
    path('product/<slug:slug>/', ProductDetailView, name='product_detail'),
    path('blog/<slug:slug>/', BlogDetailView, name='blog_detail'),
    path('cookies/', cookies, name='cookies'),
    path('product/<slug:slug>/data/', product_data, name='product_data'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

urlpatterns += staticfiles_urlpatterns()