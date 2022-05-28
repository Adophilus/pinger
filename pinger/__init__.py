import re
import subprocess as sp

ip_addr_pattern = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

def pingAddress (address):
    try:
        sp.check_call([ "ping", "-c", "1", address ])
        return True
    except Exception as e:
        return False

def separateZeros (arr, match = 0):
    zeros = [ ]
    for n in arr:
        if (match in arr):
            index = arr.index(match)
            zeros.append(index)
            arr.pop(index)
            arr.insert(index, 1)
    return zeros

def run(ip_addr):
    match = re.search(ip_addr_pattern, ip_addr)
    if (not(match)):
        return False
    ip_addr = match[0].split(".")
    ip_addr = [ int(ip) for ip in ip_addr ]
    zeros = separateZeros(ip_addr)
    ip_address = ip_addr
    active_addresses = [ ]
    for z in zeros:
        for n in range(1, 256):
            ip_address[z] = n
            address = ".".join([ str(i) for i in ip_addr ])
            if (pingAddress(address)):
                print(address, "is active")
                active_addresses.append(address)
                with open("output_file.txt", "a") as fh:
                    fh.write(address)
