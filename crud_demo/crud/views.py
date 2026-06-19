from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Conatact
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def addstudent(request):
    return render(request,'studentform.html')

def addstudentprocess(request):
    txt1=request.POST['txt1']
    txt2=request.POST['txt2']
    txt3=request.POST['txt3']
    txt4=request.POST['txt4']
    Student.objects.create(name=txt1,mobile=txt2,email=txt3,address=txt4)
    return HttpResponse('Thank You!')

def displaystudent(request):
    mystudentlist=Student.objects.all()
    return render(request,'display.html',{'mydata':mystudentlist})

def deletestudent(request,id):
    Student.objects.get(id=id).delete()
    return redirect(displaystudent)

def contact(request):
    return render(request,'contact.html')

def contactprocess(request):
    txt1 = request.POST['txt1']
    txt2 = request.POST['txt2']
    txt3 = request.POST['txt3']
    email_from= settings.EMAIL_HOST_USER
    send_mail(txt2,txt3,email_from,[txt1])
    Conatact.objects.create(email=txt1,subject=txt2,message=txt3)

    return HttpResponse("DETAILS SENT SUCCESSFULLY")