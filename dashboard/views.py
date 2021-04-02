from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
#from .models import *
from django.conf import settings

def index(request):
    return render(request, 'dashboard.html')

def details(request):
    return render(request, 'details.html')