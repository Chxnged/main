class EventManager:

    def __init__(self):
        self.listeners = {}

    def register(self, name, func):

        if name not in self.listeners:
            self.listeners[name] = []

        self.listeners[name].append(func)

    def dispatch(self, name, data):

        if name in self.listeners:
            for func in self.listeners[name]:
                func(data)
