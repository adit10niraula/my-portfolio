from django.forms import ModelForm  
from .models import  Projects,Message
from django import forms


class ProjectsModel(ModelForm):
    class Meta:
        model  = Projects
        fields = ["title", "body", "image"]
        widgets = {
            "title" :forms.TextInput(attrs={'class': 'input_form', 'placeholder': "enter the title"}),
            "body": forms.Textarea(attrs={'class': 'form_body', 'placeholder': 'enter the description'}),
            
        }


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["name", "email", "subject", "body"]

        widgets = {
            "name": forms.TextInput(attrs={'class':"input_form",'placeholder': "enter your name"}),
            "email": forms.EmailInput(attrs={'class':"input_form",'placeholder': "enter the email"}),
            "subject": forms.TextInput(attrs={'class':"input_form",'placeholder': "enter the subject"}),
            "body": forms.Textarea(attrs={'class':"form_body",'placeholder': "enter the message"}),
            
        }