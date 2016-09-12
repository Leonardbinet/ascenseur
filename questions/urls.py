from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='accueil_questions'),
    url(r'^(?P<question_name_slug>[\w\-]+)/$', views.question_lecture, name='question_lecture'),
]