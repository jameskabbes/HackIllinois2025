import typing

ABSOLUTE_MAX_MOTOR_SPEED = 100


class UnsignedSpeed(int):
    """UnsignedSpeed is a type that represents a speed value between 0 and 100."""
    def __new__(cls, value):
        if not (0 <= value <= ABSOLUTE_MAX_MOTOR_SPEED):
            raise ValueError(
                f"UnsignedSpeed must be  0>=`UnsignedSpeed`<={ABSOLUTE_MAX_MOTOR_SPEED}, got {value}")
        return super().__new__(cls, value)


class SignedSpeed(int):
    """SignedSpeed is a type that represents a speed value between -100 and 100."""
    def __new__(cls, value):
        if not (-ABSOLUTE_MAX_MOTOR_SPEED <= value <= ABSOLUTE_MAX_MOTOR_SPEED):
            raise ValueError(
                f"SignedSpeed must be {-ABSOLUTE_MAX_MOTOR_SPEED}>=`SignedSpeed`<={ABSOLUTE_MAX_MOTOR_SPEED}, got {value}")
        return super().__new__(cls, value)


class Heading(float):
    """A custom float type representing degrees from 0 to 360, where 0 is strafe right and 90 is forward"""
    def __new__(cls, value):
        if not (0 <= value < 360):
            raise ValueError(
                f"Heading must be 0<=`Heading`<360, got {value}")
        return super().__new__(cls, value)


class MotorConfig(typing.TypedDict):
    _ID: int
    _POLARITY: bool
    _FORCE_HEADING: Heading


class AxleConfig(typing.TypedDict):
    left: MotorConfig
    right: MotorConfig


class DrivetrainConfig(typing.TypedDict):
    front: AxleConfig
    rear: AxleConfig
