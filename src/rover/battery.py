import typing
from smbus2 import SMBus, i2c_msg
from rover import constants


class Battery:

    _I2C_ADDR: typing.ClassVar[int] = 0x7A
    _REGISTER: typing.ClassVar[int] = 0

    def __init__(self):
        pass

    def get_voltage(self) -> int:
        ret: int = 0
        with SMBus(constants.I2C_BUS) as bus:

            def f() -> int:
                msg = i2c_msg.write(self._I2C_ADDR, [self._REGISTER,])
                bus.i2c_rdwr(msg)
                read = i2c_msg.read(self._I2C_ADDR, 2)
                bus.i2c_rdwr(read)
                return int.from_bytes(bytes(list(read)), 'little')

            try:
                ret = f()
            except:
                ret = f()

        return ret
