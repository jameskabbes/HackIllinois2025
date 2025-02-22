import typing
from smbus2 import SMBus
from rover import constants


class LineSensors:

    _I2C_ADDR: typing.ClassVar[int] = 0x78
    _REGISTER: typing.ClassVar[int] = 0x01

    def __init__(self):
        pass

    def read(self) -> list[bool]:
        with SMBus(constants.I2C_BUS) as bus:
            value = bus.read_byte_data(self._I2C_ADDR, self._REGISTER)
            return [True if value & v > 0 else False for v in [0x01, 0x02, 0x04, 0x08]]
