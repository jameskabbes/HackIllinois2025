from rover.sonar import Sonar
import time

sonar = Sonar()
while True:
    print(sonar.get_distance())
    time.sleep(1)
