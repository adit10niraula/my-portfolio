from django.forms import ModelForm  
from .models import  Projects
from django import forms


class ProjectsModel(ModelForm):
    class Meta:
        model  = Projects
        fields = ["title", "body", "image"]
        widgets = {
            "title" :forms.TextInput(attrs={'class': 'form-title', 'placeholder': "enter the title"}),
            "body": forms.Textarea(attrs={'class': 'form-body', 'placeholder': 'enter the description'}),
            
        }