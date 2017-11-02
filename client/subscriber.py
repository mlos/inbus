import json
import socket

from shared.opcode import Opcode

class Subscriber(object):

    def __init__(self, server_address, app_key):
        self._app_key = app_key
        self._server_address = server_address
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.bind(("127.0.0.1",0))
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(self._to_outgoing_message(), server_address)


    def _to_outgoing_message(self):
        return json.dumps({'version' : 1, 'opcode' : Opcode.SUBSCRIBE, "application" : [ self._app_key, 0 ], "address" : list(self._socket.getsockname())})


    def wait_for_published_message(self):
        print "A"
        data, addr = self._socket.recvfrom(65536) # TODO config buffer size
        print data
