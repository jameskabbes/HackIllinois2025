import typing

from rover.servo import Servo
from rover.camera import Camera


class CameraSystem:

    pan_servo: Servo
    tilt_servo: Servo
    camera: Camera

    def __init__(self):
        self.pan_servo = Servo(1)
        self.tilt_servo = Servo(2)
        self.camera = Camera()
