from rover.motor import Motor
from rover import constants


class Drivetrain:
    front_left_motor: Motor
    front_right_motor: Motor
    rear_left_motor: Motor
    rear_right_motor: Motor

    def __init__(self):
        self.front_left_motor = Motor(
            constants.DRIVETRAIN['front']['left']['_ID'], constants.DRIVETRAIN['front']['left']['_POLARITY'])
        self.front_right_motor = Motor(
            constants.DRIVETRAIN['front']['right']['_ID'], constants.DRIVETRAIN['front']['right']['_POLARITY'])
        self.rear_left_motor = Motor(
            constants.DRIVETRAIN['rear']['left']['_ID'], constants.DRIVETRAIN['rear']['left']['_POLARITY'])
        self.rear_right_motor = Motor(
            constants.DRIVETRAIN['rear']['right']['_ID'], constants.DRIVETRAIN['rear']['right']['_POLARITY'])
