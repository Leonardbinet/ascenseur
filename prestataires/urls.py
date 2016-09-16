from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='accueil_prestataires'),
    url(r'^ascensoristes/',views.ascensoristes,name='ascensoristes'),
    url(r'^(?P<cat_name_slug>[\w\-]+)/$', views.categorie, name='prest_categorie'),
]