import socket
import validators


def validate_domain(domain):
    if not validators.domain(domain):
        return False
    else:
        return True

def resolve_domain_ip(data_input):
    return socket.gethostbyname(data_input)
