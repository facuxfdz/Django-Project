from django.shortcuts import render, HttpResponse
from github import Github, ContentFile
import os

# Create your views here.
def index(request):
    return render(request, 'index.html')

def proyectos(request):
    g = Github(os.environ['my_git']) #El acceso a la cuenta esta determinado por una variable de entorno del sistema
    repos = g.get_user().get_repos()
    return render(request, 'Proyectos.html', {'repos': repos})

def FAQ(request):
    return render(request, 'sobre_mi.html')
