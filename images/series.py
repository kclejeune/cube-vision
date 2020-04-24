import imageio
from os import path
from glob import glob
import numpy as np
import collections
from cv2 import cv2
from typing import List


class Image(object):
    def __init__(self, image):
        self.image = image
        self.check_image_size()

    def check_image_size(self):
        if self.image.shape[1] > 500:
            rescale_percent = 500 / self.image.shape[1]
            new_dims = (500, int(rescale_percent * self.image.shape[0]))
            self.image = cv2.resize(self.image, new_dims, interpolation=cv2.INTER_AREA)

    def convert_to_greyscale(self):
        return np.dot(self.image[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)


class Series:
    def __init__(self, series_folder):
        self.series_folder = series_folder
        self.images: List[Image] = [
            Image(imageio.imread(filename))
            for filename in glob(path.join(self.series_folder, "*"))
        ]

    def get_folder(self):
        return self.series_folder

    def __getitem__(self, key) -> Image:
        return self.images.__getitem__(key)

    def __iter__(self) -> List[Image]:
        return iter(self.images)
