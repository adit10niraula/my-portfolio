from django.shortcuts import render,redirect
from .models import Projects, Skill, Tags,Message
from .forms import ProjectsModel,MessageForm
from django.contrib import messages

# Create your views here.

def home(request):
    projects = Projects.objects.all()
    skills = Skill.objects.all()

    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            

            messages.success(request, "your message was succesfully send") 
            form = MessageForm()   

           

    
    context = {"projects":projects, "skills":skills, "form":form}


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



def inbox(request):

    messages = Message.objects.all().order_by('is_read')
    unread = Message.objects.filter(is_read = False).count()
    context = {"messages": messages, 'unread':unread}
    return render(request, 'base/inbox.html', context)


    