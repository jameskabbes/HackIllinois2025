from rover.vehicle import Vehicle
import time
import signal

if __name__ == '__main__':

    vehicle = Vehicle()

    def signal_handler(sig, frame):
        vehicle.buzzer.off()
        exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    vehicle.buzzer.on()
    time.sleep(1)
    vehicle.buzzer.off()
