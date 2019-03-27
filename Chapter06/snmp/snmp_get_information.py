#!/usr/bin/env python3

from pysnmp.hlapi import *
import sys

def get_info_snmp(host, oid):

	for (errorIndication,
         errorStatus,
         errorIndex,
         varBinds) in nextCmd(SnmpEngine(),
                              CommunityData('public'),
                              UdpTransportTarget((host, 1161)),
                              ContextData(),
                              ObjectType(ObjectIdentity(oid)),
                              lookupMib=False,
                              lexicographicMode=False):

		if errorIndication:
			print(errorIndication, file=sys.stderr)
			break

		elif errorStatus:
			print('%s at %s' % (errorStatus.prettyPrint(),
	                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'), file=sys.stderr)
			break

		else:
			for varBind in varBinds:
				print('%s = %s' % varBind)

get_info_snmp('demo.snmplabs.com', '1.3.6.1.2.1.1.9.1.2')