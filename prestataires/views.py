
# Create your views here.

from django.shortcuts import render
from django.template import loader
from .models import liste_Prestataires, Type_prestataire



def index(request):
    context = {
    }
    return render(request,'prestataires/index.html',context)


def ascensoristes(request):
    context = {
    }
    return render(request,'prestataires/section_asc.html',context)

