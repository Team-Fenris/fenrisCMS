from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='index'),
    path('dashboard/details/', views.details),


]

