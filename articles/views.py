

from django.shortcuts import render
from django.template import loader


def index(request):
    context = {
        'rien': "rien",
    }
    return render(request,'articles/index.html',context)

def articles(request):
    context = {
        'rien': "rien",
    }
    return render(request,'articles/articles.html',context)