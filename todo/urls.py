from django.urls import path
from .views import HomeView, TaskListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('tasks/', TaskListView.as_view(), name='tasks'),
]