#!/usr/bin/env python3

import ipaddress
import sys

try:
    ip = ipaddress.ip_address(sys.argv[1])
    print('%s is a correct IP%s address' % (ip, ip.version))
except ValueError:
    print('address/netmask is invalid: %s' % sys.argv[1])
except:
    print('Usage : %s  ip' % sys.argv[0])