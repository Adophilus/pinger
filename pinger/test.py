import subprocess as sp

try:
    proc = sp.check_call(["ping", "-c", "4", "192.168.43.1" ])
except sp.CalledProcessError:
    print("ip addr unreachable")
