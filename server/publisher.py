class Publisher(object):

    def __init__(self, application, payload):
        self._application = application
        self._payload = payload

    def application(self):
        return self._application

    def to_outgoing_message(self):
        return "BOGUS"

    def payload(self):
        return self._payload
