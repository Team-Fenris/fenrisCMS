
from django.db import models

# Create your models here.
class Hero(models.Model):
    
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
      return self.name

class Pcap(models.Model):
    direction = models.CharField(max_length=25, null=True)
#    dst_addr = models.CharField(max_length=15, null=True)
    dst_addr = models.GenericIPAddressField(null=False)
#    dst_port = models.CharField(max_length=5, null=True)
    dst_port = models.IntegerField(max_length=5, null=False)
    icmpv4 = models.CharField(max_length=50, null=True)
    icmpv6 = models.CharField(max_length=50, null=True)
    interface = models.CharField(max_length=5, null=True) # TODO: INT?

    ##### IPV4
    ipv4_chksum = models.IntegerField(max_length=10, null=True)
    ipv4_df = models.BooleanField(null=False, default=False)
    ipv4_diff_serv = models.PositiveSmallIntegerField(max_length=3)
    ipv4_ecn = models.PositiveSmallIntegerField(max_length=2)
    ipv4_evil = models.BooleanField(default=False)
    ipv4_flags = models.PositiveSmallIntegerField(max_length=3)
    ipv4_frag_offset = models.PositiveSmallIntegerField(max_length=2,default=0)
    ipv4_hdr_len = models.PositiveSmallIntegerField(max_length=3,default=0)
    ipv4_header_len = models.PositiveSmallIntegerField(max_length=4)
    ipv4_ident = models.PositiveSmallIntegerField(max_length=2,default=0)
    ipv4_mf = models.BooleanField(default=False)
    ipv4_packet_len = models.IntegerField(max_length=5, null=True)
    ipv4_raw = models.TextField(max_length=255)
    ipv4_reserved = models.BooleanField(default=False)
    ipv4_src_addr = models.GenericIPAddressField(null=False)
    ipv4_tos = models.PositiveSmallIntegerField(max_length=4)
    ipv4_ttl = models.PositiveSmallIntegerField(max_length=3)
#   ipv6 = models.CharField(max_length=255, null=True) # NO IPv6
    is_inbound = models.CharField(max_length=5, null=True)
    is_loopback = models.CharField(max_length=5, null=True)
    is_outbound = models.CharField(max_length=5, null=True)
    payload = models.BinaryField(null=True)
#    payload = models.CharField(max_length=255, null=True)
    raw = models.CharField(max_length=255, null=True)
    src_addr = models.CharField(max_length=15, null=True)
    src_port = models.CharField(max_length=5, null=True)
    tcp = models.CharField(max_length=255, null=True)

    # TCP
    tcp_ack = models.BooleanField(null=True)
    tcp_ack_num = models.BigIntegerField(null=True)
    tcp_chksum = models.IntegerField(max_length=10, null=True)
    tcp_control_bits = models.PositiveSmallIntegerField(max_length=3, null=True)
    tcp_cwr = models.BooleanField(null=True)
    tcp_data_offset = models.PositiveSmallIntegerField(max_length=3, null=True)
    tcp_dst_port = models.IntegerField(max_length=5, null=True)
    tcp_ece = models.BooleanField(null=True)
    tcp_fin = models.BooleanField(null=True)
    tcp_header_len = models.PositiveSmallIntegerField(null=True)
    tcp_ns = models.BooleanField(null=True)
    tcp_payload = models.BinaryField(null=True)
    tcp_psh = models.BooleanField(null=True)
    tcp_raw = models.CharField(max_length=255, null=True)
    tcp_reserved = models.PositiveSmallIntegerField(max_length=2, null=True)
    tcp_rst = models.BooleanField(null=True)
    tcp_seq_num = models.BigIntegerField(null=True)
    tcp_src_port = models.IntegerField(max_length=5, null=True)
    tcp_syn = models.BooleanField(null=True)
    tcp_urg = models.BooleanField(null=True)
    tcp_urg_ptr = models.PositiveSmallIntegerField(max_length=2, null=True)
    tcp_window_size = models.PositiveSmallIntegerField(max_length=5, null=True)

    # UDP
    udp_chksum = models.IntegerField(max_length=10, null=True)
    udp_dst_port = models.IntegerField(max_length=5, null=True)
    udp_header_len = models.PositiveSmallIntegerField(max_length=4, null=True)
    udp_payload = models.BinaryField(null=True)
    udp_payload_len = models.IntegerField(max_length=10, null=True)
    udp_raw = models.CharField(max_length=255, null=True)
    udp_src_port = models.IntegerField(max_length=5, null=True)


    udp = models.CharField(max_length=255, null=True)
    wd_addr = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.dst_addr
