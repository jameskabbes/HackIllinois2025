import typing
from rover.motor import Motor
from rover import constants, types
import math
import numpy as np


class Drivetrain:

    front_left_motor: Motor
    front_right_motor: Motor
    rear_left_motor: Motor
    rear_right_motor: Motor
    motors: list[Motor]

    def __init__(self):
        self.front_left_motor = Motor(
            constants.DRIVETRAIN['front']['left'])
        self.front_right_motor = Motor(
            constants.DRIVETRAIN['front']['right'])
        self.rear_left_motor = Motor(
            constants.DRIVETRAIN['rear']['left'])
        self.rear_right_motor = Motor(
            constants.DRIVETRAIN['rear']['right'])
        self.motors = [self.front_left_motor, self.front_right_motor,
                       self.rear_left_motor, self.rear_right_motor]

    def set_motion(self,
                   speed: types.UnsignedSpeed = types.UnsignedSpeed(0),
                   heading: types.Heading = types.Heading(90),
                   angular_speed: types.SignedSpeed = types.SignedSpeed(0)):
        """Set the motion of the rover. Speed and angular_speed are nothing more than unitless values related to the motor speed, not the physical velocity in m/s.
        if speed is set, heading must be set, and vice versa.
        """

        """
               +Y (90°)
                ↑
      (v1) ↗   [*]   ↖ (v2)
             |  |  |
 -X (180°)  [O]   [O]  +X (0°)
             |  |  |
      (v3) ↖   [*]   ↗ (v4)
                ↓
               -Y (270°)
        """

        # translational velocity
        tv = np.array([motor._FORCE_HEADING for motor in self.motors])
        tv = np.cos(np.radians(tv) - np.radians(heading))
        tv *= speed / np.max(np.abs(tv))

        # Angular velocity
        # assume counter-clockwise
        av = np.array([-angular_speed, angular_speed,
                      -angular_speed, angular_speed])

        # clockwise
        if angular_speed < 0:
            av *= 1

        v = tv + av
        v = (constants.ABSOLUTE_MAX_MOTOR_SPEED * v) / \
            (np.max([np.max(np.abs(v)), constants.ABSOLUTE_MAX_MOTOR_SPEED]))

        for i, motor in enumerate(self.motors):
            motor.set_speed(types.SignedSpeed(v[i]))

        print(v)

    def stop(self):
        """stop all motors"""

        self.front_left_motor.stop()
        self.front_right_motor.stop()
        self.rear_left_motor.stop()
        self.rear_right_motor.stop()
