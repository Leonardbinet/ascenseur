from django.shortcuts import render
from .models import Categorie, Question
# Create your views here.
def index(request):
    categories = Categorie.objects.all()
    questions = Question.objects.all()
    context = {}
    context['categories']= categories
    context['nbcat']= categories.count()
    context['questions']= questions
    return render(request,'questions/index.html',context)

def question_lecture(request, question_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        questions = Question.objects.get(slug=question_name_slug)
        context_dict['question'] = questions.question
        context_dict['reponse'] = questions.reponse
        context_dict['categorie'] = questions.categorie


    except Question.DoesNotExist:
        # We get here if we didn't find the specified article.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'questions/question_lecture.html', context_dict)

