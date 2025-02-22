import gpiozero
from rover import constants
from rover.battery import Battery
from rover.drivetrain import Drivetrain
from rover.line_sensors import LineSensors
from rover.sonar_system import SonarSystem
from rover.servo import Servo
from rover.camera_system import CameraSystem
from rpi_ws281x import PixelStrip


class Vehicle:
    buzzer: gpiozero.Buzzer
    battery: Battery
    camera_system: CameraSystem
    drivetrain: Drivetrain
    key1: gpiozero.Button
    key2: gpiozero.Button
    line_sensors: LineSensors
    sonar_system: SonarSystem
    pixel_strip: PixelStrip

    def __init__(self):

        self.buzzer = gpiozero.Buzzer(constants.BUZZER_PIN)
        self.battery = Battery()
        self.drivetrain = Drivetrain()
        self.key1 = gpiozero.Button(constants.KEY_PINS['key1'])
        self.key2 = gpiozero.Button(constants.KEY_PINS['key2'])

        self.line_sensors = LineSensors()
        self.sonar_system = SonarSystem()
        self.camera_system = CameraSystem()

        self.pixel_strip = PixelStrip(
            constants.PIXEL_STRIP['COUNT'], constants.PIXEL_STRIP['PIN'], constants.PIXEL_STRIP['FREQ_HZ'],
            constants.PIXEL_STRIP['DMA'], constants.PIXEL_STRIP[
                'INVERT'], constants.PIXEL_STRIP['BRIGHTNESS'], constants.PIXEL_STRIP['CHANNEL']
        )
