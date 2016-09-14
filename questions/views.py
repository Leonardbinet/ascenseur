from django.shortcuts import render
from .models import Categorie, Question
from .form import QuestionForm
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    #pour savoir si formulaire a ete rempli
    sauve = False

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = QuestionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            sauve = True


    # if a GET (or any other method) we'll create a blank form
    else:
        form = QuestionForm()

    categories = Categorie.objects.all()
    questions = Question.objects.filter(affichage = True)
    context = {}
    context['categories']= categories
    context['nbcat']= categories.count()
    context['questions']= questions
    context['form']= form
    context['sauve']= sauve

    return render(request,'questions/index.html',context)



