#!/usr/bin/env python3
 
import pygeoip
import argparse

def geoip_city(domain,ipaddress):
    path = 'GeoLiteCity.dat'
    gic = pygeoip.GeoIP(path)
    print(gic.record_by_addr(ipaddress))
    print(gic.region_by_name(domain))
 
def geoip_country(domain,ipaddress): 
    path = 'GeoIP.dat'
    gi = pygeoip.GeoIP(path)
    print(gi.country_code_by_name(domain))
    print(gi.country_name_by_addr(ipaddress))

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Get geolocation from domain and ip address')
	parser.add_argument('--domain', action="store", dest="domain",  default='www.packtpub.com')
	parser.add_argument('--ipaddress', action="store", dest="ipaddress",  default='83.166.169.231')
	given_args = parser.parse_args()
	domain = given_args.domain
	ipaddress = given_args.ipaddress
	geoip_city(domain,ipaddress)
	geoip_country(domain,ipaddress)
