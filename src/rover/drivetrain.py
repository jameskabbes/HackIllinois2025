from rover.motor import Motor


class Drivetrain:
    front_left_motor: Motor
    front_right_motor: Motor
    rear_left_motor: Motor
    rear_right_motor: Motor

    def __init__(self):
        self.front_left_motor = Motor('front', 'left')
        self.front_right_motor = Motor('front', 'right')
        self.rear_left_motor = Motor('rear', 'left')
        self.rear_right_motor = Motor('rear', 'right')
