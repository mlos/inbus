class Subscriber(object):

    def __init__(self, create_new_subscription, app_key):
        self._create_new_subscription = create_new_subscription
        self._app_key = app_key

    def want_to_subscribe(self):
        return self._create_new_subscription
            
    def want_to_unsubscribe(self):
        return not self.want_to_subscribe()
