from django.contrib import admin

# Register your models here.
from .models import Prestataire, Type_prestataire

admin.site.register(Prestataire)
admin.site.register(Type_prestataire)