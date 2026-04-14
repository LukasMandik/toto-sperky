from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Blog, Product, Category

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    protocol = 'https'

    def items(self):
        return Blog.objects.filter(available=True)

    def lastmod(self, obj):
        return obj.updated
    
    def location(self,obj):
        return '/blog/%s' % (obj.slug)

class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Product.objects.filter(available=True)

    def lastmod(self, obj):
        return obj.updated
    
    def location(self,obj):
        return '/product/%s' % (obj.slug)

class CategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7
    protocol = 'https'

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.updated


class GalleryCategorySitemap(Sitemap):
    """Stránky galérie podľa kategórie (/gallery/<slug>/)."""
    changefreq = "weekly"
    priority = 0.75
    protocol = 'https'

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.updated

    def location(self, obj):
        return reverse('toto_sperky_web:gallery', args=[obj.slug])


class StaticViewSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return [
            'toto_sperky_web:home',
            'toto_sperky_web:gallery_categories',
            'toto_sperky_web:blog',
            'toto_sperky_web:about_me',
            'toto_sperky_web:contact',
        ]

    def location(self, item):
        return reverse(item)

# Definovanie všetkých sitemap
sitemaps = {
    'blogs': BlogSitemap,
    'products': ProductSitemap,
    'categories': CategorySitemap,
    'gallery_categories': GalleryCategorySitemap,
    'static': StaticViewSitemap,
}