class Publisher(object):

    def __init__(self, application):
        self._application = application

    def application(self):
        return self._application
