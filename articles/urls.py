from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'rae^$', views.articles, name='articles'),
]