# ip.and.port
An ip and port scanner with the ability to scan in seconds
## Usage/Examples

```python 
import socket
from colorama import *
```

```python 
     def is_port_open(ip, port):
    """
`ip` has the `port` open
    """
    s = socket.socket()
    try:
```
```python
host=input("Enter the ip:")
for port in range(1, 1025):
    if is_port_open(host, port):
        print(f"{GREEN}[+] {host}:{port} is open      {RESET}")
    else:
```
Stop code
```bash
ctrl+c
```
Code execution
```bash
git clone https://github.com/m4rks30/ip.and.port
```
```bash
ls
```
```bash
cd ip.and.port
```
```bash
  python ips1.py
```



