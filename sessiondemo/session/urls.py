from . import views
from django.urls import path
    
urlpatterns=[    
    path('create', views.createsession),
    path('get',views.getsession),
    path('check',views.checksession),
    path('remove',views.removesession),
    path('loginpage',views.loginpage),
    path('loginprocess',views.loginprocess),
    path('dashboard',views.dashboard),
    path('logout',views.logout),
]