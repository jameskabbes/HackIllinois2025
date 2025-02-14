import typing

I2C_BUS = 1
N_SERVOS = 6


class MotorConfig(typing.TypedDict):
    _ID: int
    _POLARITY: bool


class AxleConfig(typing.TypedDict):
    left: MotorConfig
    right: MotorConfig


class DrivetrainConfig(typing.TypedDict):
    front: AxleConfig
    rear: AxleConfig


DRIVETRAIN: DrivetrainConfig = {
    "front": {
        "left": {
            "_ID": 0,
            "_POLARITY": False
        },
        "right": {
            "_ID": 1,
            "_POLARITY": True
        }
    },
    "rear": {
        "left": {
            "_ID": 2,
            "_POLARITY": False
        },
        "right": {
            "_ID": 3,
            "_POLARITY": True
        }
    }
}
