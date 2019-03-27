#!/usr/bin/env python3

import argparse
import dns.reversename
import dns.resolver

def main(address):
    name = dns.reversename.from_address(address)
    print(name)
    print(dns.reversename.to_address(name))

    try:
        # Pointer records (PTR) maps a network interface (IP) to the host name.
        domain = str(dns.resolver.query(name,"PTR")[0])
        print(domain)
    except Exception as e:
        print ("Error while resolving %s: %s" %(address, e))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DNS Python')
    parser.add_argument('--address', action="store", dest="address",  default='127.0.0.1')
    given_args = parser.parse_args() 
    address = given_args.address
    main(address)

