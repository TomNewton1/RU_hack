from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "UCAS_clear/index.html")

def register(request):
    return render(request, "UCAS_clear/register.html")

def login(request):
    return render(request, "UCAS_clear/login.html")