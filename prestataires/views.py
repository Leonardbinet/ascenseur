
# Create your views here.

from django.shortcuts import render
from django.template import loader
from .models import liste_Prestataires, Type_prestataire



def index(request):
    liste_prest = liste_Prestataires.objects.all()

    context = {
        "prestataires":liste_prest,
    }
    return render(request,'prestataires/index.html',context)


def ascensoristes(request):
    context = {
    }
    return render(request,'prestataires/section_asc.html',context)

