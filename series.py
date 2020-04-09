import imageio
from os import path
import numpy as np
import collections
from typing import Dict

cube_sides = {
    "top": "t.png",
    "front": "f.png",
    "right": "r.png",
    "left": "l.png",
    "back": "b.png",
    "down": "d.png",
}

# cube_sides = {"test": "test.png"}


class Series(collections.MutableMapping):
    def __init__(self, series_folder):
        self.images: Dict[str, Image] = {}

        for side_name, side_filename in cube_sides.items():
            self.images[side_name] = Image(path.join(series_folder, side_filename))

    def __getitem__(self, key):
        return self.images

    def __setitem__(self, key, value):
        self.images[key] = value

    def __delitem__(self, key):
        del self.images[key]

    def __iter__(self):
        return self.images.values()

    def __len__(self):
        return len(self.images)


class Image(object):
    def __init__(self, image_path: str):
        self.image_path = image_path
        self.image = imageio.imread(image_path)

    def __str__(self):
        return "<Filename: " + self.image_path.split("/")[-1] + ">"
