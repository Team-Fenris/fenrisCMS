import json
import requests
import random

class FenrisApi:
    """ Base class for Fenris API. """
    def __init__(self, api_url, api_token):
        """ Instance constructor

        :params: config: Configuration parameters for the API (yaml)
        """
#        self.api_token = config["token"]
#        self.api_url = config["url"]
        self.api_token = api_token
        self.api_url = api_url
        self.api_headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {0}'.format(self.api_token)}

    @staticmethod
    def _is_json(json_str):
        """ Check if input string is in JSON format. """
        json_str = json.dumps(json_str)
        try:
#            json_obj = json.loads(json_str)
            json.loads(json_str)
        except ValueError:
#            print(f"json_obj: {json_obj}")
            return False
        return True

    def send(self, data):
        if self._is_json(data):
            response = requests.post(self.api_url, headers=self.api_headers, json=data)
            for x in response:
                print(x)
#            print(f"Response: {response}")

        else:
            print("Error: Not a JSON string.")
            # TODO: Do JSON encoding


###### START OF APPLICATION
if __name__ == "__main__":

    # Set configuration parameters for testing and initialize object
    api_pcap_url = 'http://127.0.0.1:8000/api/pcap/'
    api_token = 'FsaGHWa312t19jgSG2qa2agsSG82gsnag383gSn2aSgn218Gxawg'
    api = FenrisApi(api_pcap_url, api_token)

    # Generate dummy data

    # Generate ints
    for x in range(1025, 1050):
        port1 = x
        port2 = x+50

    for x in range(1, 254):
        adr1 = f"192.168.{x}.100"
        adr2 = f"192.168.{x}.200"

    rand_int = random.randrange(1, 19, 2)

    json_string = {
        'direction': 'inbound',
        'dst_addr': adr1,
        'dst_port': port2,
        'icmpv4': 'icmpv4 testing',
        'icmpv6': 'icmpv6 testing',
        'interface': 'eth0',
        'ipv4_chksum': rand_int,
        'ipv4_df': True,
        'ipv4_diff_serv': rand_int,
        'ipv4_ecn': rand_int,
        'ipv4_evil': True,
        'ipv4_flags': rand_int,
        'ipv4_frag_offset': rand_int,
        'ipv4_header_len': rand_int,
        'ipv4_ident': rand_int,
        'ipv4_mf': False,
        'ipv4_packet_len': rand_int,
        'ipv4_raw': 'The quick brown fox jumped over the lazy dog.',
        'ipv4_reserved': True,
        'ipv4_src_addr': adr1,
        'ipv4_tos': rand_int,
        'ipv4_ttl': rand_int,
        'is_inbound': 'inb',
        'is_loopback': 'false',
        'is_outbound': 'true',
        # 'payload': '\xc0\xff\x00\x00\x1d',
        'raw': 'raw text',
        'src_addr': adr2,
        'src_port': port1,
        'wd_addr': 'blah blah'
    }

    api.send(json_string)
