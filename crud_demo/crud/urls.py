from . import views
from django.urls import path

urlpatterns = [
      path('studentform', views.addstudent),
      path('add-student',views.addstudentprocess),
      path('display-student',views.displaystudent),
      path('delete-student/<int:id>',views.deletestudent),
      path('contactform', views.contact),
      path('display-mail',views.contactprocess)
]