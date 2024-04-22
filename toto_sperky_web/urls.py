from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name = 'toto_sperky_web'

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery', views.gallery, name='gallery'),
    # path('<slug:category_slug>/', views.gallery, name='product_gallery_by_category'),
    path('cookies', views.cookies, name='cookies'),
]

urlpatterns += staticfiles_urlpatterns()