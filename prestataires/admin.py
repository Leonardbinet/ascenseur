from django.contrib import admin

# Register your models here.
from .models import liste_Prestataires, Type_prestataire

admin.site.register(liste_Prestataires)
admin.site.register(Type_prestataire)
