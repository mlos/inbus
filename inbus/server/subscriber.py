class Subscriber(object):

    def __init__(self, is_new_subscriber, address, app_key):
        self._is_new_subscriber = is_new_subscriber
        self._address = address
        self._app_key = app_key

    def want_to_subscribe(self):
        return self._is_new_subscriber
            
    def want_to_unsubscribe(self):
        return not self.want_to_subscribe()

    def address(self):
        return self._address

    def application_interest(self):
        return self._app_key
