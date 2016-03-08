from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='accueil_prestataires'),
    url(r'^ascensoristes/',views.ascensoristes,name='ascensoristes'),
    url(r'^focus/(?P<article_name_slug>[\w\-]+)/$', views.article_lecture, name='article_lecture'),

]