from django.contrib import admin
from .models import Projects, Skill, Tags

# Register your models here.

admin.site.register(Projects)
admin.site.register(Skill)
admin.site.register(Tags)