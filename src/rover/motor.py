import typing
from smbus2 import SMBus, i2c_msg
from rover import constants, types


class Motor:

    _I2C_ADDR: typing.ClassVar[int] = 0x7A
    _BASE_REGISTER: typing.ClassVar[int] = 31

    _ID: int
    _POLARITY: int
    _FORCE_HEADING: types.Heading
    speed: types.SignedSpeed

    def __init__(self, config: types.MotorConfig) -> None:
        self._ID = config['_ID']
        self._POLARITY = config['_POLARITY']
        self._FORCE_HEADING = config['_FORCE_HEADING']

    def forward(self, speed: types.UnsignedSpeed):
        self.set_speed(speed)

    def reverse(self, speed: types.UnsignedSpeed):
        self.set_speed(-speed)

    def stop(self):
        self.set_speed(0)

    def set_speed(self, speed: types.SignedSpeed):
        self._write_speed(speed)
        self.speed = speed

    def _write_speed(self, speed: types.SignedSpeed):
        register = Motor._BASE_REGISTER + self._ID

        if not self._POLARITY:
            speed = -speed

        with SMBus(constants.I2C_BUS) as bus:

            def f() -> None:
                msg = i2c_msg.write(
                    self._I2C_ADDR, [register, speed.to_bytes(1, 'little', signed=True)[0]])
                bus.i2c_rdwr(msg)
            try:
                f()
            except:
                f()
