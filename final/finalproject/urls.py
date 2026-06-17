from . import views
from django.urls import path

urlpatterns = [
    path('home', views.homepage),
    path('contact', views.contactpage),
    path('about', views.aboutpage),
    path('shop', views.shop),
    path('contactprocess',views.contactprocess),
]
