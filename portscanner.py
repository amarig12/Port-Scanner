import socket #using socket over nmap as this is to perfrom simple lightweight port scanning


#connection to IPv4, uses TCP packets
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #define socket object

host = input("Enter IP address: ")
"""port = input("Enter port to scan: ")"""

def portscanner(port):
    if sock.connect_ex((host, port)):
        print(f"Port {str(port)} is closed")
    else:
        print(f"Port {str(port)} is open") 

#scan ports 1 - 10
for port in range(1, 11):
    portscanner(port)