from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

from .models import Task

# Create your views here.

class HomeView(TemplateView):
    model = Task
    template_name = 'todo/index.html'
    

class TaskListView(ListView):
    model = Task


class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'priority', 'deadline']
    success_url = reverse_lazy('tasks')

class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')