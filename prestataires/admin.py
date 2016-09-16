from django.contrib import admin

# Register your models here.
from .models import Prestataire, Categorie

admin.site.register(Prestataire)
admin.site.register(Categorie)
