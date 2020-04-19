import imageio
from os import path
import numpy as np
import collections
from cv2 import cv2
from typing import Dict, List

cube_sides = {
    "top": "t.jpg",
    "front": "f.jpg",
    "right": "r.jpg",
    "left": "l.jpg",
    "back": "b.jpg",
    "down": "d.jpg",
}


class Image(object):
    def __init__(self, image_path: str):
        self.image_path = image_path

        self.image = imageio.imread(image_path)
        if self.image.shape[1] > 500:
            rescale_percent = 500 / self.image.shape[1]
            new_dims = (500, int(rescale_percent * self.image.shape[0]))
            self.image = cv2.resize(self.image, new_dims, interpolation=cv2.INTER_AREA)

    def get_greyscale(self):
        return np.dot(self.image[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)

    def get_folder(self) -> str:
        return "/".join(self.image_path.split("/")[:-1])

    def __str__(self) -> str:
        return "<Filename: " + self.image_path.split("/")[-1] + ">"


class Series(collections.MutableMapping):
    def __init__(self, series_folder):
        self.images: Dict[str, Image] = {}
        self.series_folder = series_folder

        for side_name, side_filename in cube_sides.items():
            self.images[side_name] = Image(path.join(series_folder, side_filename))

    def get_folder(self):
        return self.series_folder

    def __getitem__(self, key) -> Image:
        return self.images[key]

    def __setitem__(self, key, value):
        self.images[key] = value

    def __delitem__(self, key):
        del self.images[key]

    def __iter__(self) -> List[Image]:
        return self.images.values()

    def __len__(self) -> int:
        return len(self.images)
