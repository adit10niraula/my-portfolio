
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('projects/', views.projects, name="projects"),
    path('addprojects/', views.add_projects, name="addproject"),
    path('editprojects/<str:pk>/', views.edit_projects, name="editproject"),
    path('project/<str:pk>/', views.project, name="project"),
]