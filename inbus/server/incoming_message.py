import json

import sys

from ..shared.opcode import Opcode
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
        except:
            raise ValueError

        self._is_subscriber = self._opcode in (Opcode.SUBSCRIBE, Opcode.UNSUBSCRIBE)
        self._is_publisher = self._opcode == Opcode.PUBLISH
         
        print self._opcode
        if self._is_subscriber: 
            try:
                self._sender_address = message["address"]
            except:
                raise ValueError

        if self._is_publisher:
            try:
                self._payload = message["payload"]
            except:
                raise ValueError


    def to_subscriber(self):
        if self._is_subscriber:
            return Subscriber(self._opcode == Opcode.SUBSCRIBE, self._sender_address, self._application[0])
        else:
            return None
            

    def to_publisher(self):
        if self._is_publisher:
            return Publisher(self._application, self._payload)
        else:
            return None
