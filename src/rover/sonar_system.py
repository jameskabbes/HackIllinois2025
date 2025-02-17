import typing
from rover.sonar import Sonar
from rover import constants
from rover.constants import SONAR_PIXEL_STRIP as PS_CONST
from smbus2 import SMBus
from rpi_ws281x import PixelStrip


class SonarSystem:

    sonar: Sonar
    pixel_strip: PixelStrip

    _I2C_ADDR: typing.ClassVar[int] = 0x77
    _RGB_MODE_REGISTER: typing.ClassVar[int] = 2

    def __init__(self):
        self.sonar = Sonar()
        self.pixel_strip = PixelStrip(
            PS_CONST['COUNT'], PS_CONST['PIN'], PS_CONST['FREQ_HZ'], PS_CONST['DMA'], PS_CONST['INVERT'], PS_CONST['BRIGHTNESS'], )
        self.pixel_strip.begin()

    def setRGBMode(self, mode):
        try:
            with SMBus(constants.I2C_BUS) as bus:
                bus.write_byte_data(
                    self._I2C_ADDR, self._RGB_MODE_REGISTER, mode)
        except BaseException as e:
            print(e)

    def setPixelColor(self, index, rgb):
        try:
            if index != 0 and index != 1:
                return
            start_reg = 3 if index == 0 else 6
            with SMBus(constants.I2C_BUS) as bus:
                bus.write_byte_data(
                    self._I2C_ADDR, start_reg, 0xFF & (rgb >> 16))
                bus.write_byte_data(
                    self._I2C_ADDR, start_reg + 1, 0xFF & (rgb >> 8))
                bus.write_byte_data(
                    self._I2C_ADDR, start_reg + 2, 0xFF & rgb)
                # self.Pixels[index] = rgb
        except BaseException as e:
            print(e)

    def getPixelColor(self, index):
        if index != 0 and index != 1:
            raise ValueError("Invalid pixel index", index)
        return ((self.Pixels[index] >> 16) & 0xFF,
                (self.Pixels[index] >> 8) & 0xFF,
                self.Pixels[index] & 0xFF)

    def setBreathCycle(self, index, rgb, cycle):
        try:
            if index != 0 and index != 1:
                return
            if rgb < 0 or rgb > 2:
                return
            start_reg = 9 if index == 0 else 12
            cycle = int(cycle / 100)
            with SMBus(self.i2c) as bus:
                bus.write_byte_data(self.i2c_addr, start_reg + rgb, cycle)
        except BaseException as e:
            print(e)

    def startSymphony(self):
        self.setRGBMode(1)
        self.setBreathCycle(1, 0, 2000)
        self.setBreathCycle(1, 1, 3300)
        self.setBreathCycle(1, 2, 4700)
        self.setBreathCycle(2, 0, 4600)
        self.setBreathCycle(2, 1, 2000)
        self.setBreathCycle(2, 2, 3400)
