class Mediator:
    EVENT_TYPES = {}
    events = {}

    def __init__(self, EVENT_TYPES):
        self.EVENT_TYPES = EVENT_TYPES
        for key in self.EVENT_TYPES.keys():
            self.events.update({self.EVENT_TYPES[key]: []})

    def __del__(self):
        self.events.clear()

    def getEventTypes(self):
        return self.EVENT_TYPES

    def subscribe(self, name, func):
        if name and func:
            self.events.get(name).
