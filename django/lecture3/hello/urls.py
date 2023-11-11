from django.urls import path
from . import views #dot . means the current directory

urlpatterns = [
  path("", views.index)
]