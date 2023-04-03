from django import forms
from django.forms import ModelForm
from .models import *

class TaskForm(forms.ModelForm):
    Title = forms.CharField(label="Title", max_length=500, widget=forms.TextInput(
        attrs={'placeholder':'Enter Task Title','class':'form-control form-control-lg'}
    ))
    Complete = forms.BooleanField(widget=forms.RadioSelect())
    class Meta: 
        model = Task
        fields = [
            'Title',
        ]
        
    # def clean(self):
    #     super(Task,self).clean()
        