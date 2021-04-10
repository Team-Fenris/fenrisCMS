from rest_framework import viewsets
from .serializers import PcapSerializer, HttpSerializer, HttpsSerializer, DnsSerializer
from .models import Pcap, Http, Https, Dns
import django
from django.db.models.query import QuerySet
from django.shortcuts import render

#from django_serverside_datatable.views import ServerSideDatatableView
# from dnslib import dns
# from socket import IPV6_CHECKSUM
# from django.db.models import Sum > def dns_chart()
# from django.db.models import Sum
# from django.views.generic import TemplateView
# chartjs.views.lines works. Needed for class LineChartJSONView and Pcap - IPv4 chart in dashbaord.html
# from chartjs.views.lines import BaseLineChartView 

# Create your views here.

class PcapViewSet(viewsets.ModelViewSet):
    queryset = Pcap.objects.all().order_by('dst_addr')
    serializer_class = PcapSerializer

class HttpViewSet(viewsets.ModelViewSet):
    queryset = Http.objects.all().order_by('user_agent')
    serializer_class = HttpSerializer

class HttpsViewSet(viewsets.ModelViewSet):
    queryset = Https.objects.all().order_by('https_connection')
    serializer_class = HttpsSerializer

class DnsViewSet(viewsets.ModelViewSet):
    queryset = Dns.objects.all().order_by('dns')
    serializer_class = DnsSerializer

### BarChart.html retrieval ###

# def dns_chart(request):
#     labels = []
#     data = []

#     queryset = Pcap.objects('dst_addr').annotate(ipv4_chksum=Sum('ipv4_flags')).order_by('-dst_addr')
#     #queryset = Dns.objects.all().order_by('dst_addr')
#     for entry in queryset:
#         labels.append(entry[{'dst_addr'}])
#         data.append(entry[{'ipv4_flags'}])
    
#     return render(request, 'dashboard.html', data={
#         'labels': labels,
#         'data': data,
#     })

### Line Chart retrieval ###
### TODO: Rewrite class LineChartJSONView to retreive data from django. ###
# class LineChartJSONView(BaseLineChartView):
#     def get_labels(self):
#         """Return 7 labels for the x-axis. TODO: change to dst_addr from django.API"""
#         return ["January", "February", "March", "April", "May", "June", "July"]
#         #return render(django.__path__(Pcap.ipv4_packet_len))

#     def get_providers(self):
#         """Return names of datasets. TODO: change to ipv4_flags from django.API"""
#         return ["ipv4_packet_len", "ipv4_flags", "ipv4_ttl"]
#         #return render(django.__path__(Pcap.ipv4_flags))

#     def get_data(self):
#         """Return 3 datasets to plot. TODO: change to ipv4_ttl from django.API"""

#         return [[75, 44, 92, 11, 44, 95, 35],
#                 [41, 92, 18, 3, 73, 87, 92],
#                 [87, 21, 94, 3, 90, 13, 65]]
#         #return render(django.__path__(Pcap.ipv4_ttl))


# line_chart = TemplateView.as_view(template_name='dashboard.html')
# line_chart_json = LineChartJSONView.as_view()