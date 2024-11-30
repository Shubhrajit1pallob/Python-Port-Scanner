import nmap

nm = nmap.PortScanner()

#Target is the ip target we want to find ports on. This is the nmap website ip.
target = "45.33.32.156"

# Options are basically how we want to use nmap
# -sV give is the servers that are on that port
# -sC defines a standard nmap scan, nothing fancy.
options = "-sV -sC scan_result"

nm.scan(target, arguments=options)

for host in nm.all_hosts():
    print(f"Host: {host} ({nm[host].hostname()})")
    print(f"State: {nm[host].state()}")

    for protocol in nm[host].all_protocols():
        print(f"Protocol: {protocol}")
        port_info = nm[host][protocol]

        for port, state in port_info.items():
            print(f"Port: {port} \tState: {state}")
