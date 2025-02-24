from rover.sonar_led import SonarLEDS
import time
import signal


sonar_leds = SonarLEDS()

if __name__ == '__main__':

    def signal_handler(sig, frame):
        sonar_leds.left.setPixelColor(0)
        sonar_leds.right.setPixelColor(0)
        exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    sonar_leds.left.setPixelColor(0xFF0000)
    sonar_leds.right.setPixelColor(0x00FF00)
    time.sleep(1)
    sonar_leds.left.setPixelColor(0x00FF00)
    sonar_leds.right.setPixelColor(0xFF0000)
    time.sleep(1)
    sonar_leds.left.setPixelColor(0x0000FF)
    sonar_leds.right.setPixelColor(0xFF0000)
    time.sleep(1)
    sonar_leds.left.setPixelColor(0xFF0000)
    sonar_leds.right.setPixelColor(0x0000FF)
    time.sleep(1)

    sonar_leds.startSymphony()
    time.sleep(10)
