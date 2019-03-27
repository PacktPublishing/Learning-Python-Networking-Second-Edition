import socket

def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True

def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True
	
print("IPV4 127.0.0.1 OK:"+ str(is_valid_ipv4_address("127.0.0.1")))
print("IPV4 127.0.0.0.1 NOT OK:"+ str(is_valid_ipv4_address("127.0.0.0.1")))

print("IPV6 ::1 OK:"+ str(is_valid_ipv6_address("::1")))
print("IPV6 127.0.0.0 NOT OK:"+ str(is_valid_ipv6_address("127.0.0.0.1")))
