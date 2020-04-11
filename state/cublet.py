from typing import List
from images.series import Image


class Cublet(object):
    def __init__(self, image_position: List[int], shape: List[int]):
        self.image_position = image_position
        self.shape = shape

    def get_pixels(self, face_image: Image):
        return face_image.image[
            self.image_position[0] : self.image_position[0] + self.shape[0],
            self.image_position[1] : self.image_position[1] + self.shape[1],
        ]

    def __repr__(self):
        return "<Position: {}, Shape: {}>".format(self.image_position, self.shape)
