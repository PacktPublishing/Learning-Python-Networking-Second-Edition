#!/usr/bin/env python3

import argparse
from ldap3 import Server, Connection, ALL

def main(address):
    # Create the Server object with the given address.
    # Get ALL information.
    server = Server(address, get_info=ALL)
    #Create a connection object, and bind with auto bind set to true.
    conn = Connection(server, auto_bind=True)
    
    # Print the LDAP Server Information.
    print('******************Server Info**************')
    print(server.info)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Query LDAP Server')
    parser.add_argument('--address', action="store", dest="address",  default='ipa.demo1.freeipa.org')
    given_args = parser.parse_args() 
    address = given_args.address
    main (address)

