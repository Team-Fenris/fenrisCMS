
from django.db import models

# Create your models here.
class Pcap(models.Model):
    direction = models.CharField(max_length=25, null=True)
#    dst_addr = models.CharField(max_length=15, null=True)

    dst_addr = models.GenericIPAddressField(null=False, default='255.254.253.252')
#    dst_port = models.CharField(max_length=5, null=True)
    dst_port = models.IntegerField(null=False, default=0)

    icmpv4 = models.CharField(max_length=50, null=True)
    icmpv6 = models.CharField(max_length=50, null=True)
    interface = models.CharField(max_length=5, null=True) # TODO: INT?

    ##### IPV4
    ipv4_chksum = models.IntegerField(null=True)
    ipv4_df = models.BooleanField(null=False, default=False)

    ipv4_diff_serv = models.PositiveSmallIntegerField(null=True)
    ipv4_ecn = models.PositiveSmallIntegerField(null=True)
    ipv4_evil = models.BooleanField(default=False, null=True)
    ipv4_flags = models.PositiveSmallIntegerField(max_length=3, null=True)
    ipv4_frag_offset = models.PositiveSmallIntegerField(max_length=2,default=0, null=True)
    ipv4_hdr_len = models.PositiveSmallIntegerField(max_length=3,default=0, null=True)
    ipv4_header_len = models.PositiveSmallIntegerField(max_length=4, null=True)
    ipv4_ident = models.PositiveSmallIntegerField(max_length=2,default=0, null=True)
    ipv4_mf = models.BooleanField(default=False, null=True)
    ipv4_packet_len = models.IntegerField(max_length=5, null=True)
    ipv4_raw = models.TextField(max_length=255, null=True)
    ipv4_reserved = models.BooleanField(default=False)
    ipv4_src_addr = models.GenericIPAddressField(null=False, default='255.254.253.252')
    ipv4_tos = models.PositiveSmallIntegerField(max_length=4, null=True)
    ipv4_ttl = models.PositiveSmallIntegerField(max_length=3, null=True)
#   ipv6 = models.CharField(max_length=255, null=True) # NO IPv6

    is_inbound = models.CharField(max_length=5, null=True)
    is_loopback = models.CharField(max_length=5, null=True)
    is_outbound = models.CharField(max_length=5, null=True)
    payload = models.BinaryField(null=True)
    payload = models.CharField(max_length=255, null=True)
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

class Http(models.Model):
    http_command = models.CharField(max_length=4, null=False, default=0)
    http_path = models.CharField(max_length=255, null=False, default=0)
    request_version = models.CharField(max_length=10, null=True)
    host_generic_ip = models.GenericIPAddressField(null=True)
    user_agent = models.CharField(max_length=255, null=True)
    accept = models.CharField(max_length=255, null=True)
    accept_language = models.CharField(max_length=255, null=True)
    accept_encoding = models.CharField(max_length=255, null=True)
    http_connection = models.CharField(max_length=20, null=True)
    upgrade_insec_req = models.BooleanField(null=True)
    request_timestamp = models.DateTimeField(null=True)

    def __str__(self):

        return self.user_agent

class Https(models.Model):
    https_command = models.CharField(max_length=4, null=False, default=0)
    https_path = models.CharField(max_length=255, null=False, default=0)
    request_version = models.CharField(max_length=10, null=True)
    host_generic_ip = models.GenericIPAddressField(null=True)
    user_agent = models.CharField(max_length=255, null=True)
    accept = models.CharField(max_length=255, null=True)
    accept_language = models.CharField(max_length=255, null=True)
    accept_encoding = models.CharField(max_length=255, null=True)
    https_connection = models.CharField(max_length=20, null=True)
    upgrade_insec_req = models.BooleanField(null=True)
    request_timestamp = models.DateTimeField(null=True)

    def __str__(self):

        return self.https_connection

class Dns(models.Model):
    dns = models.CharField(max_length=5, null=False)
    query_str = models.CharField(max_length=255, null=True)
    query_type = models.IntegerField(max_length=255, null=True)
    record_type = models.CharField(max_length=5, null=True)
    dns_reply = models.TextField(max_length=255, null=True)
    request_time = models.DateTimeField(max_length=255, null=False)
    from_host_generic_ip = models.GenericIPAddressField(null=False)
    from_port = models.IntegerField(max_length=5, null=True)

    def __str__(self):

        return self.dns