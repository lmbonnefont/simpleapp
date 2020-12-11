
# TODO: get bus instance and publish on it
from time import sleep

from app.bus import get_bus


class Worker1:
	def __init__(self):
		bus = get_bus()
		bus.suscribe("main_event", self.acknowledge)

	def run(self):
		bus = get_bus()
		bus.emit("worker_1: my_event")

	def acknowledge(self, event):
		sleep(10)
		print(f"Worker1: Received event {event}")