from . import views
from django.urls import path

urlpatterns = [
      path('studentform', views.addstudent),
      path('add-student',views.addstudentprocess),
]