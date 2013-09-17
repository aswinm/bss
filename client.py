import socket

UDP_IPR = "127.0.0.2"
UDP_PORT = 5005
UDP_IPS = "127.0.0.1"


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IPR, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
