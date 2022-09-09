#! /usr/bin/python3

import nmap

scanner = nmap.PortScanner()

network = input('Please, enter the network in CIDR notationt (example: 192.168.122.0/24): ')

hosts = scanner.scan(hosts = network, arguments ='-sn')
hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]
for host, status in hosts_list:
    if status == 'up':
        print('Host:', host,'- status:', status)
