from images.series import Image
from state.cubelet import Cubelet
from typing import Dict, List
from state.constant import CubeletNames, Colors
import numpy as np


class Face(object):
    def __init__(self, face_image: Image):
        self.full_face_image = face_image

        self.face_shape: np.ndarray = None
        self.face_location: np.ndarray = None

        self.cubelets: Dict[str, Cubelet] = {
            cubelet_name: None for cubelet_name in CubeletNames.get_cubelet_order()
        }

        self.center_color = None

    def get_encoded_face(self):
        encoding = np.empty((3, 3), dtype="S1")
        for vert in range(3):
            for horiz in range(3):
                cubelet_idx = vert * 3 + horiz
                current_cubelet = self.cubelets[
                    CubeletNames.get_cubelet_by_idx(cubelet_idx)
                ]

                encoding[vert][horiz] = Colors.encode(current_cubelet.color)

        return encoding

    def get_face_image(self):
        return self.full_face_image.image[
            self.face_location[0] : self.face_location[0] + self.face_shape[0],
            self.face_location[1] : self.face_location[1] + self.face_shape[1],
        ]

    def get_cubelet_image(self, cubelet_name: str):
        return self.cubelets[cubelet_name].get_pixels(self.full_face_image)

    def set_cubelet(
        self, cubelet_name: str, cubelet_location: List, cubelet_shape: List
    ):
        self.cubelets[cubelet_name] = Cubelet(cubelet_location, cubelet_shape)

    def __getitem__(self, key):
        return self.cubelets[key]

    def __iter__(self):
        return iter(self.cubelets.values())
