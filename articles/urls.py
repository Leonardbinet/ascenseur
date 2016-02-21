from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.articles, name='articles'),
    url(r'^exemple$', views.article_exemple, name='article_exemple'),
    url(r'^(?P<article_name_slug>[\w\-]+)/$', views.article_lecture, name='article_lecture'),
]