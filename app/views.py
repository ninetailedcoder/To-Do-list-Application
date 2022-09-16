from multiprocessing import context
from django.shortcuts import render,redirect

# Create your views here.
from app.models import ToDoList

def home(request):
    tasks= ToDoList.objects.all()

    if request.method == 'POST':
        new_task=request.POST.get('new_task')
        priority= request.POST.get('priority')
        task= ToDoList(task_name=new_task, priority=priority)
        task.save()
    context={'tasks': tasks}
    return render(request, 'index.html', context)

def delete(request, pk):
    task = ToDoList.objects.get(id=pk)
    if request.method=="POST":
        task.delete()
        return redirect('home')
    context = {'task_name': task.task_name}
    return render(request, 'delete.html', context)

    