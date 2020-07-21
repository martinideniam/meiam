from django.urls import path
from .views import (homePage,
                    projectsPage)

urlpatterns = [
    path('', homePage, name='projects-home'),
    path('projects/', projectsPage, name='projects-projects')
]
