from django.db import models

# Create your models here.


class Task(models.Model):
    Title = models.CharField(max_length=500)
    Complete = models.BooleanField(default=False)
    Created_Date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Title