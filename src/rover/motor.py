import typing
from smbus2 import SMBus, i2c_msg
from rover import constants

UnsignedSpeed = int
SignedSpeed = int

Position = typing.Literal['front', 'rear']
Side = typing.Literal['left', 'right']


class Motor:

    _I2C_ADDR: typing.ClassVar[int] = 0x7A
    _BASE_REGISTER: typing.ClassVar[int] = 31

    ABSOLUTE_MAX_SPEED: typing.ClassVar[int] = 100

    _ID: int
    _POLARITY: int
    speed: SignedSpeed

    def __init__(self, _ID: int, _POLARITY: int) -> None:
        self._ID = _ID
        self._POLARITY = _POLARITY

    @staticmethod
    def apply_signed_speed_threshold(speed: SignedSpeed) -> SignedSpeed:
        return max(0, min(speed, Motor.ABSOLUTE_MAX_SPEED))

    def forward(self, speed: UnsignedSpeed):
        self._set_speed(speed)

    def reverse(self, speed: UnsignedSpeed):
        self._set_speed(-speed)

    def stop(self):
        self._set_speed(0)

    def _set_speed(self, speed: SignedSpeed):

        # apply threshold
        speed = Motor.apply_signed_speed_threshold(speed)
        register = Motor._BASE_REGISTER + self._ID
        self.speed = speed

        speed = speed if self._POLARITY else -speed
        with SMBus(constants.I2C_BUS) as bus:

            def f() -> None:
                msg = i2c_msg.write(
                    self._I2C_ADDR, [register, speed.to_bytes(1, 'little', signed=True)[0]])
                bus.i2c_rdwr(msg)

            try:
                f()
            except:
                f()
