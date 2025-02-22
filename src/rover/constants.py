from rover import types
from rover._constants import *
import gpiozero
import typing

I2C_BUS = 1


DRIVETRAIN: types.DrivetrainConfig = {
    "front": {
        "left": {
            "_ID": 1,
            "_POLARITY": False,
            "_FORCE_HEADING": types.Heading(45)

        },
        "right": {
            "_ID": 2,
            "_POLARITY": True,
            "_FORCE_HEADING": types.Heading(135)
        }
    },
    "rear": {
        "left": {
            "_ID": 3,
            "_POLARITY": False,
            "_FORCE_HEADING": types.Heading(135)
        },
        "right": {
            "_ID": 4,
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


PIXEL_STRIP: PixelStrip = {
    'COUNT': 2,
    'PIN': 12,
    'FREQ_HZ': 800000,
    'DMA': 10,
    'BRIGHTNESS': 120,
    'CHANNEL': 0,
    'INVERT': False
}

SONAR_SYSTEM_I2C_ADDR: int = 0x77

RGB_INDEX_MAPPING: dict[types.RGB_COLORS, int] = {
    'red': 0, 'green': 1, 'blue': 2}
