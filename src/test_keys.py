from rover.vehicle import Vehicle
import time

vehicle = Vehicle()

while True:
    print('Key 1: ' + str(vehicle.key1.is_active))
    print('Key 2: ' + str(vehicle.key2.is_active))
    time.sleep(1)
