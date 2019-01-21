#!/usr/bin/env python3

import ldap

LDAP_SERVER ="ldap://52.57.162.88:389"
LDAP_BASE_DN = 'ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org'
LDAP_FILTER = '(objectclass=person)'
LDAP_ATTRS = ["cn", "dn", "sn", "givenName"]
		
def main():
	try:
		# Open a connection
		ldap_client = ldap.initialize(LDAP_SERVER)
		# Set LDAPv3 option
		ldap_client.set_option(ldap.OPT_PROTOCOL_VERSION,3)
		# Bind/authenticate with a user with appropriate rights
		ldap_client.simple_bind("admin",'Secret123')
		# Get user attributes defined in LDAP_ATTRS
		result = ldap_client.search_s(LDAP_BASE_DN,ldap.SCOPE_SUBTREE,LDAP_FILTER, LDAP_ATTRS)
		print(result)
	except ldap.INVALID_CREDENTIALS as exception:
		ldap_client.unbind()
		print('Wrong username or password. '+exception)
	except ldap.SERVER_DOWN as exception:
		print('LDAP server not available. '+exception)

if __name__ == '__main__':
	main ()

