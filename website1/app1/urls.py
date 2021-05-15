
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home ') ,
    path(r'about', views.about, name='about '),
    path(r'contact', views.contact, name='contact '),
    path(r'careers', views.careers, name='careers'),
]
