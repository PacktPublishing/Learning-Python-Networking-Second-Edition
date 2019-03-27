#!/usr/bin/env python3

import argparse
import dns.zone
import dns.resolver

def main(domain):
    # IPv4 DNS Records
    answer = dns.resolver.query(domain, 'A')
    for i in range(0, len(answer)):
        print("IPV4 address: ", answer[i])

    # IPv6 DNS Records
    try:
        answer6 = dns.resolver.query(domain, 'AAAA')
        for i in range(0, len(answer6)):
            print("IPv6: ", answer6[i])
    except dns.resolver.NoAnswer as e:
        print("Exception in resolving the IPv6 Resource Record:", e)

    # MX (Mail Exchanger) Records
    try:
        mx = dns.resolver.query(domain, 'MX')
        print('Mail Servers: %s' % mx.response.to_text())
        for data in mx:
            print('Mailserver', data.exchange.to_text(), 'has preference', data.preference)
    except dns.resolver.NoAnswer as e:
        print("Exception in resolving the MX Resource Record:", e)

    # NS (Name servers) Records
    try:
        ns_answer = dns.resolver.query(domain, 'NS')
        print('Name Servers: %s' %[x.to_text() for x in ns_answer])
    except dns.resolver.NoAnswer as e:
        print("Exception in resolving the NS Resource Record:", e)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DNS Python')
    parser.add_argument('--domain', action="store", dest="domain",  default='dnspython.org')
    given_args = parser.parse_args() 
    domain = given_args.domain
    main(domain)

