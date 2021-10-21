from django.shortcuts import render



def index(request):
    return render(request, 'index.html')


def lista(request):
    return render(request, 'lista.html')


def detalhes(request):
    return render(request, 'detalhes.html')


def contato(request):
    return render(request, 'contato.html')


def login(request):
    return render(request, 'login.html')


def signin(request):
    return render(request, 'signin.html')


def adicionar(request):
    return render(request, 'adicionar.html')



