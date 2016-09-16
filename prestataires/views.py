
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


def categorie(request, cat_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        categorie_prestataire = Type_prestataire.objects.get(slug=cat_name_slug)

        context_dict['categorie'] = categorie_prestataire



    except Type_prestataire.DoesNotExist:
        # We get here if we didn't find the specified article.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'prestataires/categorie.html', context_dict)