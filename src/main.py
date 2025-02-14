from rover import motor
import time

fl_motor = motor.Motor('rear', 'right')


for i in range(0, 101):
    fl_motor._set_speed(i)
    time.sleep(0.01)

for i in range(99, -1, -1):
    fl_motor._set_speed(i)
    time.sleep(0.01)

for i in range(0, 101):
    fl_motor._set_speed(-i)
    time.sleep(0.01)

for i in range(99, -1, -1):
    fl_motor._set_speed(-i)
    time.sleep(0.01)



fl_motor.stop()
