from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            
        return redirect('/')
    
    context = {
        'tasks':tasks,
        'form':form,
    }
    
    return render(request,'tasks/list.html', context)

def updateTask(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    
    context = {
        'form':form,
    }
    return render(request, 'tasks/update_task.html',context)
    
    
def datatable(request):
    UAObject = UAWebiste.objects.all()
    title = str(UAWebiste.objects.filter(Webiste_Language=1))
    print("Title : " + title)
    if UAWebiste.objects.filter(Webiste_Language=1) == "Ministry of Electronics and Information Technology" :
        print("Hurray")
    print(UAWebiste.objects.filter(Webiste_Language=1))
    #print(UAObject.filter(Webiste_Language=))

    context = {
        'UAObject':UAObject,
    }
    return render(request,'tasks/datatable.html', context)