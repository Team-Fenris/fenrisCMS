# serializers.py
from rest_framework import serializers

from .models import Pcap, Http, Https, Dns, File


class PcapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pcap
        fields = (
            'id',
            'direction',
            'dst_addr',
            'dst_port',
            'src_addr',
            'src_port',
#            'payload',
            'protocol',
            'process_name',
            'pid',
            'request_timestamp',
        )

class HttpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Http
        fields = (
            'id',
            'http_command',
            'http_path',
            'request_version',
            'host_generic_ip',
            'user_agent',
            'accept',
            'accept_language',
            'accept_encoding',
            'http_connection',
            'upgrade_insec_req',
            'request_timestamp',            
            )

class HttpsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Https
        fields = (
            'id',
            'https_command',
            'https_path',
            'request_version',
            'host_generic_ip',
            'user_agent',
            'accept',
            'accept_language',
            'accept_encoding',
            'https_connection',
            'upgrade_insec_req',
            'request_timestamp',            
            )

class DnsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dns
        fields = (
            'id',
            'dns', 
            'query_str', 
            'query_type',
            'record_type',
            'dns_reply',
            'request_time',
            'from_host_generic_ip',
            'from_port',
            )

class FileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = File
        fields = "__all__"