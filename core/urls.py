from django.shortcuts import render
from django.urls import path
from .views import index, sticky


urlpatterns = [
    path('', index, name='index'),
    #path('', sticky, name='sticky'),

]