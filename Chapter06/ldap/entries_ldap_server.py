#!/usr/bin/env python3

from ldap3 import Server, Connection, ObjectDef, AttrDef, Reader, Writer, ALL, core

LDAP_SERVER ="ipa.demo1.freeipa.org"
LDAP_USER ="uid=admin,cn=users,cn=accounts,dc=demo1,dc=freeipa,dc=org"
LDAP_PASSWORD ="Secret123"
LDAP_FILTER = '(objectclass=person)'
LDAP_ATTRS = ["cn", "dn", "sn", "givenName"]

def main():
        # Create the Server object with the given address.
        server = Server(LDAP_SERVER, get_info=ALL)
        #Create a connection object, and bind with the given DN and password.
        try: 
                conn = Connection(server, LDAP_USER, LDAP_PASSWORD, auto_bind=True)
                print('LDAP Bind Successful.')
                # Perform a search for a pre-defined criteria.
                # Mention the search filter / filter type and attributes.
                conn.search('dc=demo1,dc=freeipa,dc=org', LDAP_FILTER , attributes=LDAP_ATTRS)
                # Print the resulting entries.
                for entry in conn.entries:
                        print(entry)
        except core.exceptions.LDAPBindError as e:
                # If the LDAP bind failed for reasons such as authentication failure.
                print('LDAP Bind Failed: ', e)

if __name__ == '__main__':
        main()

