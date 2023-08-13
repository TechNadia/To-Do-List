from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import TaskForm
from .models import TaskModel 

# Create your views here.
def home(request):
    task = TaskForm
    return render(request, 'home.html', {'form':task})

def add_task(request):
    if request.method == 'POST':
        task = TaskForm(request.POST)
        if task.is_valid:
            #print(task)
            task.save(commit=True)
            messages.success(request, "Task added successfully")
            return redirect('incomplete')        
    else:
        task = TaskForm()
    return render(request, 'home.html', {'form':task})

def incomplete_tasks(request):
        data = TaskModel.objects.filter(is_completed=False)
        return render(request, 'incomplete_tasks.html', {'data': data})

def complete_tasks(request):
    data = TaskModel.objects.filter(is_completed=True)
    return render(request, 'complete_tasks.html', {'data': data})

def make_complete(request, id):
    task = TaskModel.objects.get(pk=id)
    task.is_completed = True
    task.save()
    messages.success(request, "Kudos! Good job done!")
    data = TaskModel.objects.filter(is_completed=False)
    #render(request, 'incomplete_tasks.html', {'data': data})
    return redirect('complete')

def edit_task(request, id):
    task = TaskModel.objects.get(pk=id)
    form = TaskForm(instance=task)
    print(task.taskTitle)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        print(form.is_valid())
        if form.is_valid():
            print(id)
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect ('incomplete')
    return render(request, 'home.html', {'form': form})

def delete_task(request, id):
    task = get_object_or_404(TaskModel, pk = id)
    task.delete()
    messages.success(request, "Task deleted successfully!")
    referer = request.META.get('HTTP_REFERER')    
    return HttpResponseRedirect(referer)
    
