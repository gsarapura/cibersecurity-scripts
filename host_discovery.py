#! /usr/bin/python3

import nmap

scanner = nmap.PortScanner()

# Host discovery:
hosts = scanner.scan(hosts='192.168.0.0/24', arguments='-sn')
hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]
for host, status in hosts_list:
    if status == 'up':
        print(host, status)
