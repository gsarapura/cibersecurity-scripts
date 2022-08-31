#! /usr/bin/python

import nmap
import sys
import socket

scanner=nmap.PortScanner()

print("Bienvenido a mi primer escaneo.")
ip_addr=input("Inserte la IP por scanear: ")
print("La IP que ingreso:", ip_addr)

resp = input("""\nPor favor, seleccionar el tipo de escaneo:
            1) Escaneo TCP
            2) Escaneo UDP \n""")
print("Su selección:", resp)

if resp == '1':
    print("Version de nmap: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v') # -v goes faster.
    print(scanner.scaninfo())
    print("Estado de IP: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Puertos abiertos: ",scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print("Version de nmap: ", scanner.nmap_version())
    scanner.scan(hosts = ip_addr, arguments = '-sU -v -p 1-444')
    print(scanner.scaninfo())
    print("Estado de IP: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    # change this: print("Puertos abiertos: ",scanner[ip_addr]['udp'].keys())
    open_ports = []
    ports = scanner[ip_addr]['udp']
    for key in ports.keys():
        if ports[key]['state'] == 'open':
            open_ports.append(key)
    print("Puertos abiertos: ", open_ports)
