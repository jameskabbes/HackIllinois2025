from rover import types
from rover.types import ABSOLUTE_MAX_MOTOR_SPEED
import gpiozero
import typing

I2C_BUS = 1
N_SERVOS = 6


DRIVETRAIN: types.DrivetrainConfig = {
    "front": {
        "left": {
            "_ID": 0,
            "_POLARITY": False,
            "_FORCE_HEADING": types.Heading(45)

        },
        "right": {
            "_ID": 1,
            "_POLARITY": True,
            "_FORCE_HEADING": types.Heading(135)
        }
    },
    "rear": {
        "left": {
            "_ID": 2,
            "_POLARITY": False,
            "_FORCE_HEADING": types.Heading(135)
        },
        "right": {
            "_ID": 3,
            "_POLARITY": True,
            "_FORCE_HEADING": types.Heading(45)
        }
    }
}


class CameraServoIds(typing.TypedDict):
    pan: int
    tilt: int


CAMERA_SERVOS: CameraServoIds = {
    "pan": 1,
    "tilt": 2
}


class KeyPins(typing.TypedDict):
    key1: gpiozero.Pin
    key2: gpiozero.Pin


KEY_PINS: KeyPins = {
    "key1": 13,
    "key2": 23
}

BUZZER_PIN: gpiozero.Pin = 'BOARD31'


class PixelStrip(typing.TypedDict):
    COUNT: int
    PIN: int
    FREQ_HZ: int
    DMA: int
    BRIGHTNESS: int
    CHANNEL: int
    INVERT: bool


SONAR_PIXEL_STRIP: PixelStrip = {
    'COUNT': 2,
    'PIN': 12,
    'FREQ_HZ': 800000,
    'DMA': 10,
    'BRIGHTNESS': 120,
    'CHANNEL': 0,
    'INVERT': False
}
