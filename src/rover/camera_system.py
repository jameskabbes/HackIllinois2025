from rover.servo import Servo
from rover.camera import Camera
from rover import constants


class CameraSystem:

    pan_servo: Servo
    tilt_servo: Servo
    camera: Camera

    def __init__(self):
        self.pan_servo = Servo(constants.CAMERA_SERVOS['pan'])
        self.tilt_servo = Servo(constants.CAMERA_SERVOS['tilt'])
        self.camera = Camera()
