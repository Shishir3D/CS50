from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "hello/index.html")
def shishir(request):
    return HttpResponse("<h1 style='color:red'>Hello Shishir!</h1>")
def bob(request):
    return HttpResponse("<h1 style='color:red'>Hello Bob!</h1>")
def greet(request, name):
    return render(request, "hello/greet.html", {
        "name" : name.capitalize()
    })