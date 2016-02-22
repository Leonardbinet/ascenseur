from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='accueil_prestataires'),
    url(r'^(?P<type_prestataire_slug>[\w\-]+)/$', views.type_prestaire, name='type_prestataire'),
]