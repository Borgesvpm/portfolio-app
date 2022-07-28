from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from projects.models import Project

# Create your views here.
def all_projects(request):
    # query db to return all project objects
    projects = Project.objects.all()
    print(projects)
    return render(request, "projects/all_projects.html", {"projects": projects})


def project_detail(request, pk):
    # pk comes from urls file
    project = Project.objects.get(pk=pk)
    return render(request, "projects/detail.html", {"project": project})
