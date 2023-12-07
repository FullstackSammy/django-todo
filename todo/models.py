from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Task(models.Model):
    PRIORITIES = (
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    )
    
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    priority = models.CharField(max_length=50, choices=PRIORITIES)
    deadline = models.DateField(null=True)
    completed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['priority']
    
    def __str__(self):
        return f'{self.title} | Priority: {self.priority} | Deadline: {self.deadline}'
    

