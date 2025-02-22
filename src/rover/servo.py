import gpiozero
import typing
from smbus2 import SMBus, i2c_msg
from rover import constants, types

# Servo is a Hiwonder LFD-01


class Servo:

    _I2C_ADDR: typing.ClassVar[int] = 0x7A
    _BASE_REGISTER: typing.ClassVar[int] = 21
    _ID: types.ServoID

    def __init__(self, servo_id: types.ServoID):
        self._ID = servo_id

    def set_angle(self, angle: types.ServoAngle) -> None:
        """Set the angle of the servo motor"""

        angle = max(0, min(angle, 180))
        register = self._BASE_REGISTER + self._ID - 1
        with SMBus(constants.I2C_BUS) as bus:
            def f() -> None:
                msg = i2c_msg.write(self._I2C_ADDR, [register, angle])
                bus.i2c_rdwr(msg)
            try:
                f()
            except:
                f()
