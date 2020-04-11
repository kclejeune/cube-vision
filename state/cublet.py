from typing import List
from images.series import Image
from scipy.spatial import distance as dist
from statistics import mean
import numpy as np


class Cublet(object):
    def __init__(self, image_position: List[int], shape: List[int]):
        self.image_position = image_position
        self.shape = shape
        self.colors = {
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "blue": (0, 0, 255),
            "yellow": (255, 255, 0),
            "orange": (255, 165, 0),
            "white": (255, 255, 255)
        }

    def get_pixels(self, face_image: Image):
        return face_image.image[
            self.image_position[0]: self.image_position[0] + self.shape[0],
            self.image_position[1]: self.image_position[1] + self.shape[1],
        ]

    def __repr__(self):
        return "<Position: {}, Shape: {}>".format(self.image_position, self.shape)

    # detect if a cublet is red, green, blue, yellow, orange, or white
    def detect_color(self):
        min_dist = np.inf
        face_color = None
        for name, rgb_value in self.colors.items():
            d = dist.euclidean(rgb_value, self.image_position)
            if d < min_dist:
                min_dist = d
                face_color = name

        return face_color


cublet = Cublet([250, 150, 50], [2, 2, 3])
color = cublet.detect_color()
print(color)
