from django.contrib import admin

# Register your models here.
from .models import Prestataires, Categorie

admin.site.register(Prestataires)
admin.site.register(Categorie)
