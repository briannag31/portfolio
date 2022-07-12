from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# Create your views here.

def home(request):
    return render(request, "home.html")

def resume(request):
    return render(request, "resume.html")

def contact(request):
    return render(request, "contact.html")

def projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})

def about(request):
    return render(request, "about.html")
