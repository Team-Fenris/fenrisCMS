#from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import HeroSerializer, PcapSerializer
from .models import Hero, Pcap


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class PcapViewSet(viewsets.ModelViewSet):
    queryset = Pcap.objects.all().order_by('dst_addr')
    serializer_class = PcapSerializer

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['json']
        print(uploaded_file.name)
        print(uploaded_file.size)
    return render(request, 'dashboard.html')