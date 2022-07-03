import requests
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.say_hello, name='hme'),
    path('super/<str:check>', views.superad, name='sup'),
    path('register/', views.reg, name='reg'),
    path('process/', views.insert),
]
