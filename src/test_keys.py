import gpiozero
from rover import constants
import time

key1 = gpiozero.Button(constants.KEY_PINS['key1'])
key2 = gpiozero.Button(constants.KEY_PINS['key2'])

while True:
    print('Key 1: ' + str(key1.is_active))
    print('Key 2: ' + str(key2.is_active))
    time.sleep(1)
