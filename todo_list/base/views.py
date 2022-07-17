from django.shortcuts import render
from django.views.generic.list import ListView
from pyparsing import Optional
from requests import request
from .models import Task 
from base.models import Task

class TaskList(ListView):
    model = Task