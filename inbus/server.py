import socket
import json

from inbus_message import InbusMessage

# Listen to incoming INBUS messages

UDP_IP = "127.0.0.1"
UDP_PORT = 7222

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

clients = []


while True:
    data, addr = sock.recvfrom(65536) # buffer size is 1024 bytes
    inbus_message = None
    try:
        inbus_message = InbusMessage(data)
    except:
        print "Cannot create InbusMessage"
     
    if inbus_message.is_subscriber():
        print "subscribing ", addr
    elif inbus_message.is_publisher():
        print "publishing"
        mysock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for i in clients:
            mysock.sendto("SERVER", addr)
        print "DONE"
            
