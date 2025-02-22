from rover.sonar import Sonar
from rover.sonar_led import SonarLEDS


class SonarSystem:

    sonar: Sonar
    leds: SonarLEDS

    def __init__(self):
        self.sonar = Sonar()
        self.leds = SonarLEDS()
