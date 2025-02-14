import typing


class Sonar:

    _I2C_ADDR: typing.ClassVar[int] = 0x77
    _BASE_REGISTER: typing.ClassVar[int] = 31
