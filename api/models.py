
from django.db import models
from datetime import datetime
import base64
# https://stackoverflow.com/questions/59169700/django-db-utils-integrityerror-duplicate-key-value-violates-unique-constraint-e



# https://stackoverflow.com/questions/59169700/django-db-utils-integrityerror-duplicate-key-value-violates-unique-constraint-e
# Create your models here.
class Pcap(models.Model):
    direction = models.CharField(max_length=25, null=True)

    # Destination / Source
    dst_addr = models.GenericIPAddressField(default='255.254.253.252', null=False)
    dst_port = models.IntegerField(default=0, null=False)
    src_addr = models.GenericIPAddressField(default='255.254.253.252', null=False)
    src_port = models.IntegerField(max_length=5, default=0, null=False)
    src_addr = models.CharField(max_length=15, default=0, null=False)
    src_port = models.CharField(max_length=5, default=0, null=False)

    # _data = models.TextField(db_column='payload', null=True)
    # def set_data(self, data):
    #     self._data = base64.encodestring(data)

    # def get_data(self):
    #     return base64.decodestring(self._data)

    # payload = property(get_data, set_data)

    protocol = models.CharField(max_length=5, null=True)

    # Process
    process_name = models.CharField(max_length=100, null=True)
    pid = models.PositiveSmallIntegerField(null=True)

    # Time
    request_timestamp = models.DateTimeField(default=datetime.now(), null=True)


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
    request_timestamp = models.DateTimeField(default=datetime.now(), null=True)

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
    request_timestamp = models.DateTimeField(default=datetime.now(), null=True)

    def __str__(self):

        return self.https_connection

class Dns(models.Model):
    dns = models.CharField(max_length=5, null=False)
    query_str = models.CharField(max_length=255, null=True)
    query_type = models.IntegerField(null=True)
    record_type = models.CharField(max_length=5, null=True)
    dns_reply = models.TextField(max_length=255, null=True)
    request_time = models.DateTimeField(default=datetime.now(), null=True)
    from_host_generic_ip = models.GenericIPAddressField(null=False)
    from_port = models.IntegerField(null=True)

    def __str__(self):

        return self.dns
