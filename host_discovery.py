#! /usr/bin/python3

import nmap

scanner = nmap.PortScanner()

network = input('Please, enter the network in CIDR notation (example: 192.168.122.0/24): ')

# -sn does not do a port scan, it is a "ping scan". So, it is fast and tells you which hosts are up:
scanner.scan(hosts = network, arguments = '-sn')

# Create a list (with tuples) where "x = ip" and "nm[ip]['status']['state'] = up or down":
hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]

# Print up hosts: 
for host, status in hosts_list:
    if status == 'up':
        print('Host:', host,'- status:', status)
