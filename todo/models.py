from django.db import models

# Create your models here.

class Task(models.Model):
    PRIORITIES = (
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    )
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(max_length=50, choices=PRIORITIES)
    deadline = models.DateField(null=True)
    completed = models.BooleanField(default=False)