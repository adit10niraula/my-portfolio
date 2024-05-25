from django.shortcuts import render,redirect
from .models import Projects, Skill, Tags
from .forms import ProjectsModel

# Create your views here.

def home(request):
    projects = Projects.objects.all()
    skills = Skill.objects.all()

    context = {"projects":projects, "skills":skills}


    return render(request, "base/home.html", context)


def projects(request):
    projects = Projects.objects.all()

    context = {"projects": projects}

    return render(request, 'base/projects.html', context)


def project(request, pk):

    product = Projects.objects.get(pk=pk)

    content = {"product":product}


    return render(request, 'base/project.html', content)


def add_projects(request):
   
    form = ProjectsModel()
    if request.method == "POST":
        form = ProjectsModel(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('projects')
    content = {"form":form}
    return render(request, 'base/add_project.html', content)



def edit_projects(request, pk):

    project = Projects.objects.get(pk=pk)
    form = ProjectsModel(instance=project)

    if request.method == "POST":
        form = ProjectsModel(request.POST, request.FIlES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {"form":form}
    return render(request, 'base/add_project.html', context)

    