from rover.camera import Camera
from rover import constants
import time
import signal

camera = Camera()
if __name__ == '__main__':

    while True:
        print(camera.capture())
        print(camera.image_array)
        time.sleep(1)
