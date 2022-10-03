# This script uses the socket python in-built library to get hostname and ip address on the local network

# The socket library let's your interface with network
import socket

host = socket.gethostname()
ip_addr = socket.gethostbyname(host)

print("********************")
print("Hostname: " + host)
print("IP: " + ip_addr)
print("********************")

