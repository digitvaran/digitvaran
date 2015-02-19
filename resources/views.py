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
        data['placeholder']='Search'
    if request.method=='POST':
        searchstr=request.POST.get('searchstring')
        data['placeholder']=searchstr
        data['results']=models.Audiobook.objects.filter(description__icontains=searchstr)
    return render(request,template,data)
def browse(request):
    "Browse resources"
    data={}
    template='resources/browse.html'
    data['resources']=models.Audiobook.objects.all()
    return render(request,template,data)
