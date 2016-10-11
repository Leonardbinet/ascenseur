
# from django.shortcuts import render_to_response
# from django.template import RequestContext

from django.views.defaults import page_not_found
from django.shortcuts import render


def index(request):
    context = {
    }
    return render(request, 'index.html', context)


def my_error_404(request, exception):
    template_name = '404.html'
    return page_not_found(request, exception, template_name=template_name)
