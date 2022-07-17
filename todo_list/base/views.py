from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task 

class TaskList(ListView):
    model = Task
    

class TaskDetail(DetailView):
    model = Task
    template_name: 'base/task.html'

