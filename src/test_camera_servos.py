from rover.servo import Servo
from rover import constants
import time
import signal

pan_servo = Servo(constants.CAMERA_SERVOS['pan'])
tilt_servo = Servo(constants.CAMERA_SERVOS['tilt'])

if __name__ == '__main__':

    def signal_handler(sig, frame):
        pan_servo.set_angle(90)
        tilt_servo.set_angle(90)
        exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    print('testing pan servo')
    for i in [90, 135, 180, 135, 90, 45, 0, 45, 90]:
        pan_servo.set_angle(i)
        time.sleep(1)

    print('testing tilt servo')
    for i in [90, 135, 180, 135, 90, 45, 0, 45, 90]:
        tilt_servo.set_angle(i)
        time.sleep(1)
