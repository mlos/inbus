import socket
import json

from broadcaster import Broadcaster
from incoming_message import IncomingMessage

# Listen to incoming INBUS messages

UDP_IP = "127.0.0.1"
UDP_PORT = 7222

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

clients = []

bc = Broadcaster()

while True:
    data, addr = sock.recvfrom(65536) # buffer size is 1024 bytes
    incoming_message = None

    #try:
    incoming_message = IncomingMessage(data)
    #except:
    #    print "Cannot parse IncomingMessage"
    #    continue;

    subscriber = incoming_message.to_subscriber()
    if subscriber:
        print "SUB"
        bc.manage_subscriber(subscriber)
    else:
        publisher = incoming_message.to_publisher()
        print "PUB"
        if publisher:
            bc.broadcast_publisher(publisher)
    print "DONE"
            
