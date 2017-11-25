from django.shortcuts import render,redirect,get_object_or_404
from . import forms 
from . import models


def start(request):
    tasks=models.ToDo.objects.all()
    all_tasks=[]
    for i in tasks:
        if i.Done == False:
            all_tasks.append(i)
    context={"form":forms.ToDo,"Tasks":all_tasks}

    return render(request,"ToDo/index.html",context)
def action(request):
    Task=''
    form = forms.ToDo
    if request.method  == "POST":
        form = forms.ToDo(request.POST)
        if form.is_valid():
            Task=form.cleaned_data["ToDoInputBar"]
    models.ToDo.objects.create(aToDo=Task,Done=False)
    return redirect("/")
def delete(request,task_id):
    task = get_object_or_404(models.ToDo,id=task_id)
    task.Done=True
   
    task.save()
    return redirect("/")