import gpiozero
from rover.battery import Battery
from rover.drivetrain import Drivetrain
from rover.infrared_array import InfraredArray
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
    infrared_array: InfraredArray

    def __init__(self):

        self.buzzer = gpiozero.Buzzer(31)
        self.battery = Battery()
        self.drivetrain = Drivetrain()
        # self.key1 = gpiozero.Button(33, pull_up=True)
        # self.key2 = gpiozero.Button(35, pull_up=True)

        self.infrared_array = InfraredArray()
        self.sonar = Sonar()
        self.camera_system = CameraSystem()
