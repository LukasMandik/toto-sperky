from django.urls import path

from .views import home, gallery, ProductDetailView, cookies, product_data
# from .views import ProductDetailView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name = 'toto_sperky_web'

urlpatterns = [
    path('', home, name='home'),
    path('gallery/', gallery, name='gallery'),
    # path('<slug:category_slug>/', views.gallery, name='product_gallery_by_category'),
    path('product/<slug:slug>/', ProductDetailView, name='product_detail'),
    path('cookies/', cookies, name='cookies'),
    path('product/<slug:slug>/data/', product_data, name='product_data'),
]

urlpatterns += staticfiles_urlpatterns()