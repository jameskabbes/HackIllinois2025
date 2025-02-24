from rover.sonar_led import SonarLEDS
import time

sonar_leds = SonarLEDS()
while True:
    sonar_leds.startSymphony()
