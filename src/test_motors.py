from rover.drivetrain import Drivetrain
from rover.motor import Motor
import time
import signal


if __name__ == '__main__':

    drivetrain = Drivetrain()

    def signal_handler(sig, frame):
        drivetrain.front_left_motor.stop()
        drivetrain.front_right_motor.stop()
        drivetrain.rear_left_motor.stop()
        drivetrain.rear_right_motor.stop()
        exit(0)

    def motor_test(motor: Motor):
        print('forward')
        for i in range(0, 100, 1):
            motor.forward(i)
            time.sleep(0.5 / 100)
        for i in range(99, 0, -1):
            motor.forward(i)
            time.sleep(0.5 / 99)
        print('reverse')
        for i in range(0, 100, 1):
            motor.reverse(i)
            time.sleep(0.5 / 100)
        for i in range(99, 0, -1):
            motor.reverse(i)
            time.sleep(0.5 / 99)
        motor.stop()

    signal.signal(signal.SIGINT, signal_handler)

    print('testing front left motor')
    motor_test(drivetrain.front_left_motor)
    print('testing front right motor')
    motor_test(drivetrain.front_right_motor)
    print('testing rear left motor')
    motor_test(drivetrain.rear_left_motor)
    print('testing rear right motor')
    motor_test(drivetrain.rear_right_motor)
