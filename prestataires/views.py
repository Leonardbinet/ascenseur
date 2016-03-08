
# Create your views here.

from django.shortcuts import render
from django.template import loader
from .models import liste_Prestataires, Type_prestataire, pre_Article



def index(request):
    context = {
    }
    return render(request,'prestataires/index.html',context)


def ascensoristes(request):
    context = {
    }
    return render(request,'prestataires/section_asc.html',context)

def article_lecture(request, article_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        article = pre_Article.objects.get(slug=article_name_slug)
        context_dict['nom_article'] = article.titre_article
        context_dict['description_article'] = article.description
        context_dict['body_article'] = article.body


    except pre_Article.DoesNotExist:
        # We get here if we didn't find the specified article.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'prestataires/article_lecture.html', context_dict)