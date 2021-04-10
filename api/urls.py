# myapi/urls.py

from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.views import APIView

from .views import line_chart, line_chart_json

router = routers.DefaultRouter()

router.register(r'pcap', views.PcapViewSet)
router.register(r'http', views.HttpViewSet)
router.register(r'https', views.HttpsViewSet)
router.register(r'dns', views.DnsViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # dns-chart > barchart.html
    #path('dns-chart/', views.dns_chart, name='dns-chart'),
    path('chart', line_chart, name='line_chart'),
    path('chartJSON', line_chart_json, name='line_chart_json'),
]
