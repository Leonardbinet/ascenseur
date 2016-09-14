from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='accueil_prestataires'),
    url(r'^ascensoristes/',views.ascensoristes,name='ascensoristes'),
]