
class Broadcaster(object):

    def __init__(self):
        self._subscribers = []

    def manage_subscriber(self, subscriber):
        if subscriber.want_to_subscribe():
            self._subscribers.append(subscriber)
        elif subscriber.want_to_unsubscribe():
            self._subscribers = [s for s in self._subscribers if s.address() != subscriber.address()]
            
    def broadcast_publisher(self, publisher):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        addresses = [s.address() for s in self._subscribers if s.application_interest() == publisher.application()]
        for addr in addresses:
            mysock.sendto("SERVER", addr)
