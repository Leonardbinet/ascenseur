from django.shortcuts import render
# from django.template import loader
from .models import Article, Categorie


def index(request):
    categories = Categorie.objects.all()
    articles = Article.objects.all()
    context = {'categories': categories, 'nbcat': categories.count(),
               'articles': articles}
    return render(request, 'articles/index.html', context)


def article_lecture(request, article_name_slug):
    # Create a context dictionary which we can pass to the template rendering
    # engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        article = Article.objects.get(slug=article_name_slug)
        context_dict['article'] = article

    except Article.DoesNotExist:
        # We get here if we didn't find the specified article.
        # Don't do anything - the template displays the "no category" message
        # for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'articles/article.html', context_dict)
