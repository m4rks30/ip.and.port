# ip.and.port
#An ip and port scanner with the ability to scan in seconds
#fuck_you_editpr
import socket
from colorama import *
init()
GREEN=Fore.GREEN
RESET=Fore.RESET
GRAY=Fore.LIGHTBLACK_EX
def is_port_open(ip, port):
    """
`ip` has the `port` open
    """
    s = socket.socket()
    try:
        s.connect((ip, port))
        s.settimeout(0.2)
    except:
        return False
    else:
        return True
ip=input("Enter the ip:")
for port in range(1, 1025):
    if is_port_open(ip, port):
        print(f"{GREEN}[+] {ip}:{port} is open      {RESET}")
    else:
        print(f"{GRAY}[!] {ip}:{port} is closed    {RESET}", end="\r")
