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
            'ipv4',
            'ipv6',
            'is_inbound',
            'is_loopback',
            'is_outbound',
            'payload',
            'raw',
            'src_addr',
            'src_port',
            'tcp',
            'udp',
            'wd_addr'
        )