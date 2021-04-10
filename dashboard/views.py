#from .views import Dns
from typing import Annotated
from django.db.models.base import Model
from django.db.models.fields import IntegerField
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from dnslib import dns
from .models import *
from django.conf import settings
from django.db.models import Sum



def index(request):
    return render(request, 'dashboard.html')

def details(request):
    return render(request, 'details.html')