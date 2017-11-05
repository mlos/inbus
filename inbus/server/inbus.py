import socket

from broadcaster import Broadcaster
from incoming_message import IncomingMessage

class Inbus(object):

    def __init__(self, address=("127.0.0.1", 7222), buffer_size=65536):
        self._address = address
        self._buffer_size = buffer_size
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.bind(address)
        self._broadcaster = Broadcaster()

    def run(self):
        while True:
            try:
                self._listen_and_process_message()
            except:
                pass
            print "NEXT"


    def _listen_and_process_message(self):
        data, addr = self._socket.recvfrom(self._buffer_size)
        incoming_message = None

        try:
            incoming_message = IncomingMessage(data)
        except:
            raise

        subscriber = incoming_message.to_subscriber()
        if subscriber:
            bc.manage_subscriber(subscriber)
            del subscriber
        else:
            publisher = incoming_message.to_publisher()
            if publisher:
                bc.broadcast_publisher(publisher)
                del publisher

        del incoming_message
