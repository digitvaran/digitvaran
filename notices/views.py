from django.shortcuts import render,get_object_or_404,redirect
from datetime import timedelta
from notices import models
from django.utils import timezone

def home(request):
    "Redirect to 0 delta timeperiod view"
    return redirect('notices:timeperiod_view',delta=0)


def success_save(request):
    data={}
    template='notices/success.html'
    return render(request,template,data)


def new_notice(request):
    data={}
    template='notices/new.html'
    if request.method=='GET':
        data['form']=models.NoticeForm()
    if request.method=='POST':
        form=models.NoticeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notices:successful_save')
        else:
            data['form']=form
    return render(request,template,data)

def timeperiod(request,delta):
    "Show notices with zero day delta"
    data={}
    template='notices/home.html'
    now=timezone.now()
    othertime=now+timedelta(int(delta))
    if othertime<now:
        start=othertime
        end=now
    else:
        start=now
        end=othertime
    notices=models.Notice.objects.filter(publish_date__lte=timezone.now(),event_date__lte=end,event_date__gte=start)
    data['notices']=notices
    data['timeperiod']=delta
    return render(request,template,data)
