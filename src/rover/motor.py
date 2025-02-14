import typing
from smbus2 import SMBus, i2c_msg
from rover import constants

UnsignedSpeed = int
SignedSpeed = int

Position = typing.Literal['front', 'rear']
Side = typing.Literal['left', 'right']


class Motor:

    ABSOLUTE_MAX_SPEED: typing.ClassVar[int] = 100
    __ADDR: typing.ClassVar[int] = 31

    _ID: int
    _POLARITY: int

    def __init__(self, position: Position, side: Side):

        if position == 'front':
            if side == 'left':
                self._ID = 0
                self._POLARITY = True
            elif side == 'right':
                self._ID = 1
                self._POLARITY = False
        elif position == 'rear':
            if side == 'left':
                self._ID = 2
                self._POLARITY = True
            elif side == 'right':
                self._ID = 3
                self._POLARITY = False

    @staticmethod
    def apply_signed_speed_threshold(speed: SignedSpeed) -> SignedSpeed:
        return max(0, min(speed, Motor.ABSOLUTE_MAX_SPEED))

    def set_speed(self, speed: UnsignedSpeed, forward: bool):
        thresholded_speed = Motor.apply_signed_speed_threshold(speed)
        if not forward:
            thresholded_speed = -thresholded_speed

        self._set_speed(thresholded_speed)

    def _set_speed(self, speed: SignedSpeed):

        reg = Motor.__ADDR + self._ID
        speed = speed if self._POLARITY else -speed

        with SMBus(constants.I2C) as bus:
            msg = i2c_msg.write(constants.I2C_ADDR, [
                                self._ID, speed, self._POLARITY])
            bus.i2c_rdwr(msg)
