import json
import socket

from shared.opcode import Opcode

class Publisher(object):

    def __init__(self, server_address, app_key):
        self._app_key = app_key
        self._server_address = server_address
        
    def publish(self, payload):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print self._to_outgoing_message(payload)
        sock.sendto(self._to_outgoing_message(payload), self._server_address)

    def _to_outgoing_message(self, payload):
        return json.dumps({'version' : 1, 'opcode' : Opcode.PUBLISH, "application" : [ self._app_key, 0 ], "payload" : payload })

        

