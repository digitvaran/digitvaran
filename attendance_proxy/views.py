from django.shortcuts import render
from attendance_proxy.functions import get_attendance

def home(request):
    data={}
    template='attendance_proxy/home.html'
    return render(request,template,data)

def attendance(request,prog,sem,mm):
    data={}
    template='attendance_proxy/attendance.html'
    prog,sem,mm=int(prog),int(sem),int(mm)
    students,subjects=get_attendance(prog,sem,mm)
    data['subjects']=subjects
    data['students']=students
    return render(request,template,data)
