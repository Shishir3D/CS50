from django.shortcuts import render
from django import forms

task = ['apple', 'octopus', 'rhino']

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

def index(request):
    return render(request, 'tasks/index.html', {
       "tasks" : task 
    })

def addtask(request):
    return render(request, 'tasks/add.html', {
        "form" : NewTaskForm()
    })