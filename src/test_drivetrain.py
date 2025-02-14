from rover.drivetrain import Drivetrain
import time

drivetrain = Drivetrain()

print('front left motor forward')
drivetrain.front_left_motor.forward(50)
time.sleep(1)
print('front left motor reverse')
drivetrain.front_left_motor.reverse(50)
time.sleep(1)
drivetrain.front_left_motor.stop()
