from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request,"home.html")

def contactpage(request):
    return render(request,"contact.html")

def aboutpage(request):
    return render(request,"about.html")

def shop(request):
    return render(request,"shop.html")

def contactprocess(request):
    a= int(request.POST["txt1"])
    b= int(request.POST["txt2"])
    c= a + b
    msg="A is ",a ,"B is ",b ,"Sum is ",c
    d=""
    if c==50:
        d = "C is equal to 50"
    elif c>50:
        d = "C is greater than 50"
    else:
        d = "C is smaller than 50"
    return render(request,"ans.html",{'mya':a,'myb':b,'myc':c,'myd':d})