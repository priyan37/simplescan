# Developed by Priyadharshan Vadivel
import socket

socket.setdefaulttimeout(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input("Enter target IP or hostname: ")
port = int(input("Enter port to scan: "))

result = s.connect_ex((target, port))

if result == 0:
    print(f"Port {port} is OPEN")
else:
    print(f"Port {port} is CLOSED")

s.close()

