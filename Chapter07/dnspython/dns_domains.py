#!/usr/bin/env python3

import dns.name

domain1= dns.name.from_text('python.org')
domain2 = dns.name.from_text('pypi.python.org')

print(domain2.is_subdomain(domain1))
print(domain2.is_superdomain(domain1))  

