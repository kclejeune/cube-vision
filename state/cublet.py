from typing import List
import numpy as np
from images.series import Image


class Cublet(object):
    def __init__(self, cublet_location: List[int], cublet_shape: List[int]):
        self.cublet_location = cublet_location
        self.cublet_shape = cublet_shape

        self.color: str = ""

    def get_pixels(self, face_image: Image):
        return face_image.image[
            self.cublet_location[0] : self.cublet_location[0] + self.cublet_shape[0],
            self.cublet_location[1] : self.cublet_location[1] + self.cublet_shape[1],
        ]

    def __repr__(self):
        return "<Position: {}, cublet_shape: {}>".format(
            self.cublet_location, self.cublet_shape
        )
