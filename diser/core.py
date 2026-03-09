from .events import EventManager
from .http_client import HTTP

class App:

    def __init__(self, token):
        self.token = token
        self.events = EventManager()
        self.http = HTTP(token)

    def listen(self, event):

        def wrapper(func):
            self.events.register(event, func)
            return func

        return wrapper

    def start(self):
        print("[Diser.py] Your bot has been started!")
