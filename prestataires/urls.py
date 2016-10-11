from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='accueil_prestataires'),
    url(r'^(?P<cat_name_slug>[\w\-]+)/$',
        views.categorie, name='prest_categorie'),
    url(r'^prestataire/(?P<prest_name_slug>[\w\-]+)/$',
        views.prestataire, name='prestataire'),
]
