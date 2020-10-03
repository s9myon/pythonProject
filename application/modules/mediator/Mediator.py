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

    # подписаться на событие
    def subscribe(self, name, func):
        if name and func:
            self.events.get(name).append(func)

    # дёрнуть события (вызвать все колбеки, которые в него прописаны)
    def call(self, name, data=None):
        if name:
            cbs = self.events.get(name)
            if cbs:
                for cb in cbs:
                    cb(data)
