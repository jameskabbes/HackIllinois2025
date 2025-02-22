import typing

from rover import _constants


class Bounded[T]:
    MIN: T
    MAX: T

    def __new__(cls, value):
        if not (cls.MIN <= value <= cls.MAX):
            raise ValueError(
                f"{cls.__name__} must be {cls.MIN}>=`{cls.__name__}`<={cls.MAX}, got {value}")
        return super().__new__(cls, value)


class BoundedInt(Bounded[int]):
    pass


class BoundedFloat(Bounded[float]):
    pass


class UnsignedSpeed(BoundedInt):
    MIN = 0
    MAX = _constants.ABSOLUTE_MAX_MOTOR_SPEED


class SignedSpeed(BoundedInt):
    MIN = -_constants.ABSOLUTE_MAX_MOTOR_SPEED
    MAX = _constants.ABSOLUTE_MAX_MOTOR_SPEED


class ServoID(BoundedInt):
    MIN = 1
    MAX = _constants.N_SERVOS


class ServoAngle(BoundedInt):
    MIN = 0
    MAX = 180


class SonarLEDID(BoundedInt):
    MIN = 1
    MAX = _constants.N_SONAR_LEDS


class MotorID(BoundedInt):
    MIN = 1
    MAX = _constants.N_MOTORS


class Heading(BoundedFloat):
    MIN = 0.0
    MAX = 360.0


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


RGB_COLORS = typing.Literal['red', 'green', 'blue']
