from typing import List
import numpy as np
from images.series import Image


class Cubelet(object):
    def __init__(self, cubelet_location: List[int], cubelet_shape: List[int]):
        self.cubelet_location = cubelet_location
        self.cubelet_shape = cubelet_shape

        self.color: str = ""

    def get_pixels(self, face_image: Image):
        return face_image.image[
            self.cubelet_location[0] : self.cubelet_location[0] + self.cubelet_shape[0],
            self.cubelet_location[1] : self.cubelet_location[1] + self.cubelet_shape[1],
        ]

    def __repr__(self):
        return "<Position: {}, cubelet_shape: {}>".format(
            self.cubelet_location, self.cubelet_shape
        )
