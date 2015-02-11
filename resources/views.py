from django.shortcuts import render
from resources import models

def home(request):
    "Homepage for requests"
    data={}
    template='resources/home.html'
    return render(request,template,data)
def search(request):
    "Searching for resources"
    data={}
    template='resources/search.html'
    if request.method=='GET':
        pass
    if request.method=='POST':
        data['results']=models.Tag.objects.all()
    return render(request,template,data)
