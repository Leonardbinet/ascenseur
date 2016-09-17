
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.shortcuts import render


def index(request):
    context = {
    }
    return render(request,'index.html',context)



