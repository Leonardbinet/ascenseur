from django.contrib import admin

from .models import Question, Categorie

admin.site.register(Question)
admin.site.register(Categorie)