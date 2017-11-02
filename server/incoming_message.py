import json

from shared.opcode import Opcode
from subscriber import Subscriber
from publisher import Publisher

class IncomingMessage(object):
    
    def __init__(self, data):

        try:
            message = json.loads(data)
        except:
            raise ValueError

        try:
            self._version = message["version"]
            self._opcode = message["opcode"]
            self._application = message["application"]
            self._sender_address = message["address"]
            self._payload = message["payload"]
        except:
            raise ValueError

    def to_subscriber(self):
        if self._opcode in (Opcode.SUBSCRIBE, Opcode.UNSUBSCRIBE):
            return Subscriber(self._opcode == Opcode.SUBSCRIBE, self._sender_address, self._application[0])
        else:
            return None
            
    def to_publisher(self):
        if self._opcode == Opcode.PUBLISH:
            return Publisher(self._application, self._payload)
        else:
            return None
