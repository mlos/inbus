
class Broadcaster(object):

    def __init__(self):
        self._subscribers = []

    def manage_subscriber(self, subscriber):
        if subscriber.want_to_subscribe():
            self._subscribers.append(subscriber)
        elif subscriber.want_to_unsubscribe():
            self._subscribers = [s for s in self._subscribers if s.id() != subscriber.id()]
            
    def broadcast_publisher(self, publisher):
        for subscriber in self._subscribers:
            pass
            
