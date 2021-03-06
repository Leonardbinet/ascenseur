"""ascenseur URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import ArticleSitemap, PrestatairesSitemap, StaticViewSitemap
from django.views.generic.base import TemplateView
from os import environ
from importlib import import_module

handler404 = 'ascenseur.views.my_error_404'

urlpatterns = [
    url(r'^$', views.index, name="accueil"),
    url(r'^articles/', include('articles.urls')),
    url(r'^prestataires/', include('prestataires.urls')),
    url(r'^questions/', include('questions.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^robots\.txt', TemplateView.as_view(template_name='robots.txt')),
    url(r'^sitemap\.xml$', sitemap, {
        'sitemaps': {
            'articles': ArticleSitemap,
            'presataires': PrestatairesSitemap,
            'static': StaticViewSitemap
        }
    }, name='django.contrib.sitemaps.views.sitemap')
]


current_settings = import_module(environ['DJANGO_SETTINGS_MODULE'])

if current_settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': current_settings.MEDIA_ROOT, }),
    )
