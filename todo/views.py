from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Task

# Create your views here.

class HomeView(TemplateView):
    model = Task
    template_name = 'todo/index.html'
    

class TaskListView(ListView):
    model = Task
    
