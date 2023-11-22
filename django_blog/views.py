from django.http import HttpResponse 
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello world")
    return render(request, 'home.html')


def about(request): 
    # return HttpResponse("About page here..")
    return render(request, 'about.html')