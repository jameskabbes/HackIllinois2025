from rover import motor
import time

fl_motor = motor.Motor('front', 'left')


for i in range(0, 110, 10):
    fl_motor.set_speed(i, True)
    time.sleep(0.5)

for i in range(100, -10, 10):
    fl_motor.set_speed(i, True)
    time.sleep(0.5)
