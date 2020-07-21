from django.shortcuts import render
from .models import projectsPost
# Create your views here.


def homePage(request):
    template_name = 'projects/index.html'
    return render(request, template_name)


def projectsPage(request):
    context = {'projects': projectsPost.objects.all()}
    template_name = 'projects/projects.html'
    return render(request, template_name, context)
