# serializers.py
from rest_framework import serializers

from .models import Pcap, Http, Https, Dns


class PcapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pcap
        fields = (
            'id',
            'direction',
            'dst_addr',
            'dst_port',
            'icmpv4',
            'icmpv6',
            'interface',
            'ipv4_chksum',
            'ipv4_df',
            'ipv4_diff_serv',
            'ipv4_ecn',
            'ipv4_evil',
            'ipv4_flags',
            'ipv4_frag_offset',
            'ipv4_header_len',
            'ipv4_ident',
            'ipv4_mf',
            'ipv4_packet_len',
            'ipv4_raw',
            'ipv4_reserved',
            'ipv4_src_addr',
            'ipv4_tos',
            'ipv4_ttl',
            'is_inbound',
            'is_loopback',
            'is_outbound',
            'payload',
            'raw',
            'src_addr',
            'src_port',
            'wd_addr'
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