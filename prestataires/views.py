
# Create your views here.

from django.shortcuts import render
from django.template import loader
from .models import Prestataire, Type_prestataire



def index(request):
    context = {
    }
    return render(request,'prestataires/index.html',context)


def type_prestaire(request, type_prestataire_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        type_prestataire = Type_prestataire.objects.get(slug=type_prestataire_slug)
        context_dict['nom_type_prestataire'] = type_prestataire.nom_categorie
        context_dict['description_prestataire'] = type_prestataire.description

        # Retrieve all of the associated prestataires.
        # Note that filter returns >= 1 model instance.
        prestataires = Prestataire.objects.filter(categorie=type_prestataire)

        # Adds our results list to the template context under name pages.
        context_dict['prestataires'] = prestataires
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        #context_dict['category'] = category


    except Type_prestataire.DoesNotExist:
        # We get here if we didn't find the specified article.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'prestataires/type_prestataires.html', context_dict)

