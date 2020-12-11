from app.bus import get_bus
from app.worker1 import Worker1
from app.worker2 import Worker2


def main():
	worker_1 = Worker1()
	worker_2 = Worker2()
	bus = get_bus()
	bus.emit("main_event")

if __name__ == "__main__":
	main()