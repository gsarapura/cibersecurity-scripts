# It is not recommended since it is slow and time-consuming.
# However, "nmap -ns <network/>" did not recongise all active hosts until a ping was executed.
# Only 253 since:
# xx.xx.xx.0 is for the network.
# xx.xx.xx.1 is for the gateway.
# xx.xx.xx.255 is for the broadcast.

#! /usr/bin/python3
import platform
import subprocess

def myping(host):
    parameter = '-n' if platform.system().lower()=='windows' else '-c'

    command = ['ping', parameter, '1', host]
    response = subprocess.call(command)
    
    return response

active_ips_octet = []
def ping253():
    """
    """
    for i in range(1,254):
        response = myping("192.168.0."+str(i))
        if response == 0:
            active_ips_octet.append(i)

ping253()
print("The IPs active (last octect):", active_ips_octet)
