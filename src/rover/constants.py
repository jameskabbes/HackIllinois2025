import gpiozero
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


class CameraServoIds(typing.TypedDict):
    pan: int
    tilt: int


CAMERA_SERVOS: CameraServoIds = {
    "pan": 0,
    "tilt": 1
}


class KeyPins(typing.TypedDict):
    key1: gpiozero.Pin
    key2: gpiozero.Pin


KEY_PINS: KeyPins = {
    "key1": 13,
    "key2": 23
}
