import gpiozero
from rover import constants
from rover.battery import Battery
from rover.drivetrain import Drivetrain
from rover.line_sensors import LineSensors
from rover.sonar import Sonar
from rover.servo import Servo
from rover.camera_system import CameraSystem


class Vehicle:
    buzzer: gpiozero.Buzzer
    battery: Battery
    camera_system: CameraSystem
    drivetrain: Drivetrain
    key1: gpiozero.Button
    key2: gpiozero.Button
    infrared_array: LineSensors

    def __init__(self):

        self.buzzer = gpiozero.Buzzer(constants.BUZZER_PIN)
        self.battery = Battery()
        self.drivetrain = Drivetrain()
        self.key1 = gpiozero.Button(constants.KEY_PINS['key1'])
        self.key2 = gpiozero.Button(constants.KEY_PINS['key2'])

        self.infrared_array = LineSensors()
        self.sonar = Sonar()
        self.camera_system = CameraSystem()
