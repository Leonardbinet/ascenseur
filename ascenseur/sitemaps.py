from django.contrib.sitemaps import Sitemap
from django.contrib import sitemaps
from django.core.urlresolvers import reverse
from articles.models import Article
from prestataires.models import Prestataire



class ArticleSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Article.objects.all()


class PrestatairesSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Prestataires.objects.all()


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1
    changefreq = 'monthly'

    def items(self):
        return ['accueil', 'accueil_articles', 'accueil_prestataires']

    def location(self, item):
        return reverse(item)

