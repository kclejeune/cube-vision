from images.series import Image
from state.cublet import Cublet
from typing import Dict, List
from state.constant import CubletNames, Colors
import numpy as np


class Face(object):
    def __init__(self, face_image: Image):
        self.full_face_image = face_image

        self.face_shape: np.ndarray = None
        self.face_location: np.ndarray = None

        self.cublets: Dict[str, Cublet] = {
            cublet_name: None for cublet_name in CubletNames.get_cublet_order()
        }

        self.center_color = None

    def get_encoded_face(self):
        encoding = np.empty((3, 3), dtype="S1")
        for vert in range(3):
            for horiz in range(3):
                cublet_idx = vert * 3 + horiz
                current_cublet = self.cublets[CubletNames.get_cublet_by_idx(cublet_idx)]

                encoding[vert][horiz] = Colors.encode(current_cublet.color)

        return encoding

    def get_face_image(self):
        return self.full_face_image.image[
            self.face_location[0] : self.face_location[0] + self.face_shape[0],
            self.face_location[1] : self.face_location[1] + self.face_shape[1],
        ]

    def get_cublet_image(self, cublet_name: str):
        return self.cublets[cublet_name].get_pixels(self.full_face_image)

    def set_cublet(self, cublet_name: str, cublet_location: List, cublet_shape: List):
        self.cublets[cublet_name] = Cublet(cublet_location, cublet_shape)

    def __getitem__(self, key):
        return self.cublets[key]

    def __iter__(self):
        return iter(self.cublets.values())
