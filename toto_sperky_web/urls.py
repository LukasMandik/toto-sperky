from django.urls import path

from .views import home, gallery, ProductDetailView, cookies, product_data, about_me, contact, blog_view, BlogDetailView, category_detail, UserLoginView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LogoutView
app_name = 'toto_sperky_web'

urlpatterns = [
    path('', home, name='home'),
    path('gallery/', gallery, name='gallery'),
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