from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    return render(request,"newyear/index.html", {
        "date" : newyearcheck()
    } )
    
def newyearcheck():
    dateAndTime = datetime.datetime.now()
    return dateAndTime.month == 1     and dateAndTime.day == 1
