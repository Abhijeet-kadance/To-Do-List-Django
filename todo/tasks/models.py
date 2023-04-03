from django.db import models
from django.contrib import admin

# Create your models here.


class Task(models.Model):
    Title = models.CharField(max_length=500)
    Complete = models.BooleanField(default=False)
    Created_Date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Title
    
# Language = (
#         ('', '-- Select --'),
#         ('ENGLISH', 'English'),
#         ('HINDI', 'Hindi'), 
#         ('MARATHI', 'Marathi'),
#         )

class Language(models.Model):
    Language_Title = models.CharField(max_length=300,null=True,default="")
    
    def __str__(self):
        return self.Language_Title

class UAWebiste(models.Model):
    Website_Title = models.CharField(max_length=500)
    Webiste_Language = models.ForeignKey(Language, on_delete=models.CASCADE , default="")
    Webiste_URL = models.CharField(max_length=500)
    
    def __str__(self):
        return self.Website_Title
        
# class UAReady(models.Model):
#     Website_Title = models.CharField(max_length=300)
#     Website_URL = models.CharField(max_length=500)
#     Languages = models.
#     # Languages = models.CharField(max_length=15, choices=Language, default="")
    
#     def __str__(self):
#         return self.Website_Title
    
# class Languages(models.Model):
#     Languages = models.ForeignKey(UAReady, on_delete=models.CASCADE , default="")
#     Language_Related_To = models.CharField(max_length=15, choices=Language,default="")
#     Language_Url = models.CharField(max_length=500)
 
 
#     def __str__(self):
#         return self.Languages.Website_Title
    


    
