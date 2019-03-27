#!/usr/bin/env python3

import requests

class IPtoGeo(object):

    def __init__(self, ip_address):
        # Initialize objects to store
        self.latitude = ''
        self.longitude = ''
        self.country = ''
        self.city = ''
        self.ip_address = ip_address
        self._get_location()

    def _get_location(self):

        json_request = requests.get('http://api.hostip.info/get_json.php?ip=%s&position=true' % self.ip_address).json()
        if 'country_name' in json_request:
            self.country = json_request['country_name']
        if 'country_code' in json_request:
            self.country_code = json_request['country_code']
        if 'city' in json_request:
            self.city = json_request['city']
        if 'lat' in json_request:
            self.latitude = json_request['lat']
        if 'lng' in json_request:
            self.longitude = json_request['lng']

if __name__ == '__main__':
    geolocation = IPtoGeo('8.8.8.8')
    print(geolocation.__dict__)