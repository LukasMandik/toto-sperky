"""
URL configuration for toto_sperky project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from toto_sperky_web import views
from django.contrib.sitemaps.views import sitemap
from toto_sperky_web.sitemaps import BlogSitemap, ProductSitemap, CategorySitemap, StaticViewSitemap
from django.views.generic import TemplateView
sitemaps = {
    'blogs': BlogSitemap,
    'products': ProductSitemap,
    'categories': CategorySitemap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gallery/', views.gallery, name='gallery'),
    path('', include('toto_sperky_web.urls')),
    path('search/', views.search_results, name='search_results'),
    path('search_suggestions/', views.search_suggestions, name='search_suggestions'),  # Pridanie tejto línie
    path('add_blog/', views.add_blog, name='add_blog'),
    path('blog/<slug:slug>/update/', views.update_blog, name='update_blog'),
    path('blog/<slug:slug>/delete/', views.delete_blog, name='delete_blog'),
    path('add_product/', views.add_product, name='add_product'),
    path('product/<slug:slug>/update/', views.update_product, name='update_product'),
    path('product/<slug:slug>/delete/', views.delete_product, name='delete_product'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:slug>/update/', views.update_category, name='update_category'),
    path('category/<slug:slug>/delete/', views.delete_category, name='delete_category'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)