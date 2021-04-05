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

# class AddPcapView(viewsets.ModelViewSet):
#     form_class = PcapForm
#     template_name = 'add_pcap.html'

#     def get(self, request; *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {'form': form})
# #        return HttpResponse('result')

#     def post(self, request, *args, **kwargs):
#         form = self.form.class(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('/success/')

#         return render(request, self.template_name, {'form': form})