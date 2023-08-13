from django import forms
from . import models

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = models.TaskModel
        exclude = ['id', 'is_completed']
        fields = ['taskTitle', 'taskDescription']
        labels = {
            'taskTitle': 'Title', 
            'taskDescription': 'Description'   
        }
