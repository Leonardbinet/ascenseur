from django.contrib.sitemaps import Sitemap
from django.contrib import sitemaps
from django.core.urlresolvers import reverse
from articles.models import Article
from prestataires.models import liste_Prestataires



class ArticleSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Article.objects.all()


class PrestatairesSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return liste_Prestataires.objects.all()


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['accueil', 'accueil_articles', 'accueil_prestataires']

    def location(self, item):
        return reverse(item)

