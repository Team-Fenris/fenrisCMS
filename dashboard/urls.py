from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='index'),
    path('dashboard/details/', views.details),
    path('dashboard/dns/', views.dns),
    path('dashboard/http/', views.http),
    path('dashboard/https/', views.https),
    path('', views.index, name='index'),
]

