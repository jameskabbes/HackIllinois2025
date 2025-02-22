from rover.line_sensors import LineSensors
import time
import signal
import sys


if __name__ == '__main__':

    infrared_array = LineSensors()

    def signal_handler(sig, frame):
        print('Exiting gracefully...')
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        print(infrared_array.read())
        time.sleep(1)
