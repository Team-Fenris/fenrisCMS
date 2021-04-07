# serializers.py
from rest_framework import serializers

from .models import Hero, Pcap

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')

class PcapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pcap
        fields = (
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