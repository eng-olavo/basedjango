from django.shortcuts import render
from django.urls import path
from .views import index, contato, detalhes, lista, login, signin


urlpatterns = [
    path('', index, name='index'),
    path('/contato', contato, name='contato'),
    path('/detalhes', detalhes, name='detalhes'),
    path('/lista', lista, name='lista'),
    path('/login', login, name='login'),
    path('/signin', signin, name='signin'),
]