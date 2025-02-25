import typing
from picamera2 import Picamera2
import numpy as np


class Camera:
    cam: Picamera2
    image_array: np.ndarray

    def __init__(self):

        self.image_array = np.ndarray(0)

        try:
            self.cam = Picamera2()
            self.cam.start(show_preview=False)
        except:
            self.cam = None

    def capture(self):

        if self.cam != None:
            self.image_array = self.cam.capture_array()
