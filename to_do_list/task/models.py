from django.db import models

# Create your models here.
class TaskModel(models.Model):
    id = models.AutoField(primary_key=True)
    taskTitle = models.CharField(max_length=50)
    taskDescription = models.TextField() 
    is_completed = models.BooleanField(default = False)
    
    def __str__(self) -> str:
        return f"{self.taskTitle}"
