#Packet sniffer in Python
import socket

#create an INET, raw packet

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

#receive a packet
while True:
    print s.recvfrom(65565)
    
    