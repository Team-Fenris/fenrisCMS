from django.contrib import admin
from .models import Pcap, Http, Https, Dns, File

# Register your models here.
admin.site.register(Pcap)
admin.site.register(Http)
admin.site.register(Https)
admin.site.register(Dns)
admin.site.register(File)
