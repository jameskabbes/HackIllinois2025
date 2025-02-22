import typing
from smbus2 import SMBus, i2c_msg
from rover import constants, types


class SonarLED:
    _ID: types.SonarLEDID
    _BASE_RGB_COLOR_REG = 3
    _BASE_RGB_BREATHING_CYCLE_REG = 9

    def __init__(self, led_id: types.SonarLEDID):
        self._ID = led_id

    def setPixelColor(self, rgb):
        try:
            start_reg = self._BASE_RGB_COLOR_REG + (3 * (self._ID - 1))
            with SMBus(constants.I2C_BUS) as bus:
                bus.write_byte_data(
                    constants.SONAR_SYSTEM_I2C_ADDR, start_reg, 0xFF & (rgb >> 16))
                bus.write_byte_data(
                    constants.SONAR_SYSTEM_I2C_ADDR, start_reg + 1, 0xFF & (rgb >> 8))
                bus.write_byte_data(
                    constants.SONAR_SYSTEM_I2C_ADDR, start_reg + 2, 0xFF & rgb)
        except BaseException as e:
            print(e)

    def setBreathCycle(self, rgb_color: types.RGB_COLORS, cycle):
        try:
            start_reg = self._BASE_RGB_BREATHING_CYCLE_REG + \
                (3 * (self._ID - 1))
            with SMBus(constants.I2C_BUS) as bus:
                bus.write_byte_data(
                    constants.SONAR_SYSTEM_I2C_ADDR, start_reg + constants.RGB_INDEX_MAPPING[rgb_color], int(cycle / 100))
        except BaseException as e:
            print(e)


class SonarLEDS:
    left: SonarLED
    right: SonarLED

    _RGB_MODE_REGISTER: typing.ClassVar[int] = 2

    def __init__(self):
        self.left = SonarLED(types.SonarLEDID(1))
        self.right = SonarLED(types.SonarLEDID(2))

    def setRGBMode(self, mode):
        try:
            with SMBus(constants.I2C_BUS) as bus:
                bus.write_byte_data(
                    constants.SONAR_SYSTEM_I2C_ADDR, self._RGB_MODE_REGISTER, mode)
        except BaseException as e:
            print(e)

    def startSymphony(self):
        self.setRGBMode(1)
        self.left.setBreathCycle('red', 2000)
        self.left.setBreathCycle('green', 3300)
        self.left.setBreathCycle('blue', 4700)
        self.right.setBreathCycle('red', 4600)
        self.right.setBreathCycle('green', 2000)
        self.right.setBreathCycle('blue', 3400)
