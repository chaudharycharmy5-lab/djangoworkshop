from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.
def createsession(request):
    request.session['username']="ABC"
    return HttpResponse("Session Created")

def getsession(request):
    a =request.session['username']
    return HttpResponse(a)

def checksession(request):
    if request.session.has_key('username'):
        a =request.session['username']
        return HttpResponse(a)
    else:
        return HttpResponse("Session Expired")

def removesession(request):
    del request.session['username']
    return HttpResponse("Session Removed")

def loginpage(request):
    return render(request,'login.html')

def loginprocess(request):
    a = request.POST['mail']
    request.session['myemail']= a
    return redirect(dashboard)

def dashboard(request):
    if request.session.has_key('myemail'):
        return render(request,'dashboard.html')
    else:
        return redirect(loginpage)

def logout(request):
    del request.session['myemail']
    return redirect(loginpage)

def mailsend(request):
    subject = 'Django Mail Demo'
    message = ' Hello How are you ?'
    email_from= settings.EMAIL_HOST_USER
    recipient_list= ['abc@gmail.com']
    send_mail( subject, message, email_from , recipient_list)
    return HttpResponse("Mail Sent")

def counter(request):
    if "count" not in request.session:
        request.session["count"] = 0

    request.session["count"] += 1

    return HttpResponse("Count = " + str(request.session["count"]))

def contactpageview(request):
    return render(request,'contact.html')

def mailsendprocess (request):
    subject =request.POST ['txt2']
    message =request.POST ['txt3']
    recipient_list=[ request.POST ['txt1'],]
    email_from= settings.EMAIL_HOST_USER
    send_mail( subject, message, email_from , recipient_list)
    return HttpResponse ("Mail Sent")
