from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='accueil_articles'),
    url(r'^(?P<article_name_slug>[\w\-]+)/$',
        views.article_lecture, name='article_lecture'),
]
