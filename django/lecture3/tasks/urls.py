from django.urls import path
from . import views

app_name = "tasks" #app_name is a django keyword
urlpatterns = [
    path('', views.index, name = 'index'),
    path('add', views.addtask, name = 'add')
]