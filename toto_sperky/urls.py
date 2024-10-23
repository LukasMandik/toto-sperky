
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
    path('', include('toto_sperky_web.urls')),
    path('admin/', admin.site.urls),
   
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
