from django.shortcuts import render,redirect
from django.http import HttpResponse

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