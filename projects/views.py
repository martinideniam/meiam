from django.shortcuts import render

# Create your views here.


def homePage(request):
    template_name = 'projects/index.html'
    return render(request, template_name)
