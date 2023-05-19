import socket
host = input("Enter IP address to scan: ")
port = int(input("Enter port number to scan: "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
result = s.connect_ex((host, port))
if result == 0:
    print(f"Port {port} is open on {host}")
else:
    print(f"Port {port} is closed on {host}")
s.close()
