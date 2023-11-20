from django.shortcuts import render

task = ['apple', 'octopus', 'rhino']

def index(request):
    return render(request, 'tasks/index.html', {
       "tasks" : task 
    })

def addtask(request):
    return render(request, 'tasks/add.html')