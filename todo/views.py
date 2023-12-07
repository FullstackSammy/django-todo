from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Task

# Create your views here.

class HomeView(TemplateView):
    model = Task
    template_name = 'todo/index.html'
    

class TaskListView(ListView):
    model = Task


class TaskDetailView(DetailView):
    model = Task
    
