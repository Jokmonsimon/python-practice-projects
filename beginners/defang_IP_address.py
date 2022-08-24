# Defang IP Address

import ipaddress


def ip_address(address):
    new_address = ""
    split_address = address.split(".")
    separator = "[.]"
    new_address = separator.join(split_address)
    return new_address
ipaddress = ip_address("127.100.0.0")

print(ipaddress)