from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse('<h1>Hello world!</h1>')

def aboutpage(request):
    return HttpResponse('<h3>About Us!</h3>')

def contactpage(request):
    return HttpResponse('<h2>Contact Us!<h2/>')

def gallerypage(request):
    return HttpResponse('<h2>Gallery Page!</h2>')
    