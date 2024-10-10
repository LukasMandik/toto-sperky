from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Blog, Product, Category

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Blog.objects.filter(available=True)

    def lastmod(self, obj):
        return obj.updated

class ProductSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Product.objects.filter(available=True)

    def lastmod(self, obj):
        return obj.updated

class CategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.updated

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return [
            'toto_sperky_web:home',
            'toto_sperky_web:gallery',
            'toto_sperky_web:blog',
            'toto_sperky_web:about_me',
            'toto_sperky_web:cookies'
        ]

    def location(self, item):
        return reverse(item)

# Definovanie všetkých sitemap
sitemaps = {
    'blogs': BlogSitemap,
    'products': ProductSitemap,
    'categories': CategorySitemap,
    'static': StaticViewSitemap,
}