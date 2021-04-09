from django.shortcuts import render
from rest_framework import viewsets
## imports for file upload ##
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import PcapSerializer, HttpSerializer, HttpsSerializer, DnsSerializer, FileSerializer
from .models import Pcap, Http, Https, Dns, File

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

class FileUploadView(APIView):
    permission_classes = []
    http_method_names = ['get', 'head', 'post']
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        file_serializer = FileSerializer (data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        


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
# uncomment to add POST method.
# def upload(request):
#     if request.method == 'POST':
#         uploaded_file = request.FILES['json']
#         print(uploaded_file.name)
#         print(uploaded_file.size)
#     return render(request, 'dashboard.html')

