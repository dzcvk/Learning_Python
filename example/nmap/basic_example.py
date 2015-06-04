import nmap                         # import nmap.py module
nm = nmap.PortScanner()         # instantiate nmap.PortScanner object
#nm.scan(hosts='192.168.1.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
nm.scan(hosts='192.168.1.0/24', arguments='-p 80')
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
for host, status in hosts_list:
    print('{0}:{1}'.format(host, status))
