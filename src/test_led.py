from rover.sonar_system import SonarSystem
import time

from rpi_ws281x import PixelStrip
from rpi_ws281x import Color as PixelColor

if __name__ == '__main__':

    sonar_system = SonarSystem()

    def signal_handler(sig, frame):
        exit(0)

    sonar_system.setRGBMode(1)
    time.sleep(1)
    sonar_system.setPixelColor(0, PixelColor(255, 0, 0))
    sonar_system.setPixelColor(1, PixelColor(255, 0, 0))
    time.sleep(1)
    sonar_system.setPixelColor(0, PixelColor(0, 255, 0))
    sonar_system.setPixelColor(1, PixelColor(0, 255, 0))
    time.sleep(1)
    sonar_system.setPixelColor(0, PixelColor(0, 0, 255))
    sonar_system.setPixelColor(1, PixelColor(0, 0, 255))
    time.sleep(1)
    sonar_system.setPixelColor(0, PixelColor(0, 0, 0))
    sonar_system.setPixelColor(1, PixelColor(0, 0, 0))
