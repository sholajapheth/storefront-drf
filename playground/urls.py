from django.urls import path, include 
from . import views

#url configuration
urlpatterns = [
    path('hello/', views.say_hello)
]