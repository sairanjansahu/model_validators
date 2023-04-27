from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    to=Topicform()
    d={'to':to}
    if request.method=='POST':
        tod=Topicform(request.POST)
        if tod.is_valid():
            tod.save()
            return HttpResponse('INSERTION DONE SUCCESFULLY')
        else:
            return HttpResponse('DATA IS INVALID')
    return render(request,'insert_topic.html',d)