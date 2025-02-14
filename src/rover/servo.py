import typing
from smbus2 import SMBus, i2c_msg
from rover import constants

ServoID = int  # 1-6
Degrees = int  # 0-180


class Servo:

    _I2C_ADDR: typing.ClassVar[int] = 0x7A
    _BASE_REGISTER: typing.ClassVar[int] = 21
    _CMD_REGISTER: typing.ClassVar[int] = 40

    _ID: int

    def __init__(self, servo_id: ServoID):

        if servo_id < 1 or servo_id > constants.N_SERVOS:
            raise AttributeError("Invalid servo ID {}, must be between 1 and {}".format(
                servo_id, constants.N_SERVOS))

        self._ID = servo_id

    def set_angle(self, angle: Degrees):

        angle = max(0, min(angle, 180))
        register = Servo._BASE_REGISTER + self._ID - 1

        with SMBus(constants.I2C_BUS) as bus:

            def f() -> None:
                msg = i2c_msg.write(self._I2C_ADDR, [register, angle])
                bus.i2c_rdwr(msg)
                # __servo_angle[index] = angle
                # __servo_pulse[index] = int(((200 * angle) / 9) + 500)

            try:
                f()
            except:
                f()
