
class Broadcaster(object):

    def __init__(self):
        self._subscribers = []

    def manage(self, subscriber):
        if subscriber.want_to_subscribe():
            pass
        elif subscriber.want_to_unsubscribe():
            pass
            
    def broadcast(self, publisher):
        for subscriber in self._subscribers:
            pass
            
