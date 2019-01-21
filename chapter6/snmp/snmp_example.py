#!/usr/bin/env python3

from pysnmp.entity.rfc3413.oneliner import cmdgen

SNMP_HOST = 'demo.snmplabs.com'
SNMP_PORT = 161
SNMP_COMMUNITY = 'public'

if __name__ == '__main__':
	cmd_generator = cmdgen.CommandGenerator()
	
	error_notify, error_status, error_index, var_binds = cmd_generator.getCmd(cmdgen.CommunityData(SNMP_COMMUNITY),
	cmdgen.UdpTransportTarget((SNMP_HOST, SNMP_PORT)),
	cmdgen.MibVariable('SNMPv2-MIB', 'sysDescr', 0),
	lookupNames=True, lookupValues=True)
	
	# Check for errors and print out results
	if error_notify:
		print(error_notify)
	elif error_status:
		print(error_status)
	else:
		for name, val in var_binds:
			print('%s = %s' % (name.prettyPrint(),val.prettyPrint()))
