import json

from subscriber import Subscriber
from publisher import Publisher

class IncomingMessage(object):

    OPCODE_SUBSCRIBE = 1
    OPCODE_UNSUBSCRIBE = 2
    OPCODE_PUBLISH = 3
    
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
        if self._opcode in (self.OPCODE_SUBSCRIBE, self.OPCODE_UNSUBSCRIBE):
            return Subscriber(self._opcode == self.OPCODE_SUBSCRIBE, self._application[0])
        else:
            return None
            
    def to_publisher(self):
        if self._opcode == self.OPCODE_PUBLISH:
            return Publisher()
        else:
            return None
