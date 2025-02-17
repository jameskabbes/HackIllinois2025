from rpi_ws281x import PixelStrip as WSPixelStrip


class PixelStrip(WSPixelStrip):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
