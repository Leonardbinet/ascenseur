from django.contrib import admin

# Register your models here.
from .models import Article, Categorie

admin.site.register(Article)
admin.site.register(Categorie)