
# TODO: get bus instance and publish on it
from time import sleep

from app.bus import get_bus


class Worker2:
	def __init__(self):
		bus = get_bus()
		bus.suscribe("main_event", self.acknowledge)

	def run(self):
		bus = get_bus()
		bus.emit("worker_2: my_event")

	def acknowledge(self, event):
		sleep(10)
		print(f"Worker2: Received {event}")