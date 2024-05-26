from django.db import models
import uuid
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=200)
    body =RichTextUploadingField()
    slug = models.SlugField(null=True, blank=True)
    created =models.DateTimeField(auto_now_add =True)
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True)
    image = models.ImageField(upload_to = 'projects/')

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True)

    def __str__(self):
        return self.title

class Tags(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
 
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True)
    
    def __str__(self):
        return self.name


class Message(models.Model):
    name= models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add = True)
    subject = models.CharField(max_length = 200, null=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True)
    