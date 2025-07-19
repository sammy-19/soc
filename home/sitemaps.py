from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return ['home:home', 'home:about', 'home:programs', 'home:events', 'home:blog', 'home:causes', 'home:contact']

    def location(self, item):
        return reverse(item)
