#! /usr/bin/python
# Required installation:
# pip => https://pip.pypa.io/en/stable/installation/
# nmap => pip install python-nmap

import nmap

scanner = nmap.PortScanner()

print("*** Bienvenido a mi primer escaneo ***")
ip_addr = input("Inserte la IP por scanear: ")
print("La IP que ingresó:", ip_addr)

resp = input("""\nPor favor, seleccionar el tipo de escaneo:
            1) Escaneo TCP
            2) Escaneo UDP \n""")
print("Su selección:", resp)

if resp == '1':
    print("Version de nmap: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v') # -v goes faster.
    print(scanner.scaninfo())
    print("Estado de IP: ", scanner[ip_addr].state())
    if scanner[ip_addr].all_protocols() != []:
        print("Puertos abiertos: ",scanner[ip_addr]['tcp'].keys())
    else:
        print("Los puertos están cerrados.")
elif resp == '2':
    print("Version de nmap: ", scanner.nmap_version())
    scanner.scan(hosts = ip_addr, arguments = '-sU -v -p 1-1024') # UDP scan takes quiet some time, be patient.
    print(scanner.scaninfo())
    print("Estado de IP: ", scanner[ip_addr].state())
    open_ports = []
    ports = scanner[ip_addr]['udp']
    for key in ports.keys():
        if ports[key]['state'] == 'open':
            open_ports.append(key)
    if open_ports != []:
        print("Puertos abiertos: ", open_ports)
    else:
        print("Los puertos están cerrados.")
else:
    print("Ingrese una opción correcta")
