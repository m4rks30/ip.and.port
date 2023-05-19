import nmap
from tqdm import tqdm

host = input("Enter IP address to scan: ")
ports = input("Enter port numbers to scan (separated by comma): ")
ports = [int(p) for p in ports.split(",")]

nm = nmap.PortScanner()
for port in tqdm(ports):
nm.scan(hosts=host, arguments=f"-p {port}", sudo=True)
state = nm[host]["tcp"][port]["state"]
if state == "open":
    print(f"Port {port} is open on {host}")
else:
    print(f"Port {port} is closed on {host}")
