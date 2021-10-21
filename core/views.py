from django.shortcuts import render



def index(request):
    return render(request, 'index.html')



def sticky(request):
    return render(request, 'sticky.html')
