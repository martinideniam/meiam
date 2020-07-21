from django.shortcuts import render
from .models import projectsPost
# Create your views here.


def homePage(request):
    template_name = 'projects/index.html'
    if len(projectsPost.objects.all()) >= 1:
        context = {'projects': projectsPost.objects.all()}
    else:
        context = {'projects': None}
    return render(request, template_name, context)
