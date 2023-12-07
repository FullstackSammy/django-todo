from django.urls import path
from .views import HomeView, TaskListView, TaskDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='task-detail'),
]