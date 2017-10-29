import json

class InbusMessage(object):

    OPCODE_SUBSCRIBE = 1
    OPCODE_UNSUBSCRIBE = 2
    OPCODE_PUBLISH = 3
    
    def __init__(data):
        try:
            message = json.loads(data)
        except:
            raise ValueError

        try:
            self._opcode = message["opcode"]
            self._version = message["version"]
            self._app_key = message["app-key"]
            self._app_type = message["app-type"]
            self._sender_addr = message["address"]
            self._payload = message["playload"]
        except:
            raise ValueError

    def is_subscriber(self):
        return self._opcode in (OPCODE_SUBSCRIBE, OPCODE_UNSUBSCRIBE)
            
    def is_publisher(self):
        return self._opcode in (OPCODE_PUBLISH)
