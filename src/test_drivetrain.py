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

    signal.signal(signal.SIGINT, signal_handler)

    print('forward')
    drivetrain.set_motion(speed=100, heading=90)
    time.sleep(2)

    print('reverse')
    drivetrain.set_motion(speed=100, heading=270)
    time.sleep(2)

    print('strafe right')
    drivetrain.set_motion(speed=100, heading=0)
    time.sleep(2)

    print('strafe left')
    drivetrain.set_motion(speed=100, heading=180)
    time.sleep(2)

    print('45 heading')
    drivetrain.set_motion(speed=100, heading=45)
    time.sleep(2)

    print('315 heading')
    drivetrain.set_motion(speed=100, heading=315)
    time.sleep(2)

    print('225 heading')
    drivetrain.set_motion(speed=100, heading=225)
    time.sleep(2)

    print('135 heading')
    drivetrain.set_motion(speed=100, heading=135)
    time.sleep(2)

    print('rotate counter-clockwise')
    drivetrain.set_motion(angular_speed=100)
    time.sleep(2)

    print('rotate clockwise')
    drivetrain.set_motion(angular_speed=-100)
    time.sleep(2)

    print('drift1')
    drivetrain.set_motion(speed=100, heading=180, angular_speed=100)
    time.sleep(5)

    print('drift2')
    drivetrain.set_motion(speed=100, heading=0, angular_speed=-100)
    time.sleep(5)

    drivetrain.set_motion(speed=0, heading=0, angular_speed=0)
    time.sleep(1)
