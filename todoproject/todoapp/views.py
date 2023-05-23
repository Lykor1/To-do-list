from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import TodoListItem

def todoappView(request):
    all_items = TodoListItem.objects.all()
    return render(request, 'todoapp/todolist.html', {'all_items':all_items})

def addTodoView(request):
    content = request.POST['content']
    date = request.POST['date']
    time = request.POST['time']
    new_item = TodoListItem(content = content, date=date, time=time)
    new_item.save()
    return HttpResponseRedirect(reverse('todolist'))

def deleteTodoView(request, pk):
    item = TodoListItem.objects.get(pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('todolist'))