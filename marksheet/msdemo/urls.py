from msdemo import views
from django.urls import path

urlpatterns = [
    path('marksheet', views.msheet),
]
