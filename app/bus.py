# Develop a singleton instance of a bus
# which can emit events
from collections import defaultdict
from time import sleep


class Bus:
    def __init__(self):
        self.subscriptions = defaultdict(lambda: [])
    def emit(self, event):
        print(event)
        print("This is the subscription list")
        print(self.subscriptions)
        if event == "main_event":
            for callback in self.subscriptions[event]:
                callback(event)

    def suscribe(self, event, call_back):
        self.subscriptions[event].append(call_back)

_bus = None
def get_bus():
    global _bus
    if not _bus:
        _bus = Bus()
    return _bus