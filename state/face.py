from images.series import Image
from state.cublet import Cublet
from typing import Dict, List
from state.constant import CubletNames, Colors
import numpy as np


class Face(object):
    def __init__(self, face_image: Image):
        self.face_image = face_image

        self.face_shape: np.ndarray = None
        self.face_location: np.ndarray = None

        self.cublets: Dict[str, Cublet] = {
            cublet_name: None for cublet_name in CubletNames.get_cublet_order()
        }

        self.face_color = None

    def get_cublet_image(self, cublet_name: str):
        return self.cublets[cublet_name].get_pixels(self.face_image)

    def set_cublet(self, cublet_name: str, image_position: List, shape: List):
        self.cublets[cublet_name] = Cublet(image_position, shape)

    def set_face_color(self, color: str):
        self.face_color = color
