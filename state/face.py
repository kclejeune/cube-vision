from images.series import Image
from state.cublet import Cublet
from typing import Dict, List

cublet_names = ["TL", "TC", "TR", "ML", "MC", "MR", "BL", "BC", "BR"]


class Face(object):
    def __init__(self, face_image: Image):
        self.face_image = face_image

        self.face_shape = None
        self.face_location = None

        self.cublets: Dict[str, Cublet] = {
            cublet_name: None for cublet_name in cublet_names
        }

    def get_cublet_image(self, cublet_name: str):
        return self.cublets[cublet_name].get_pixels(self.face_image)

    def set_cublet(self, cublet_name: str, image_position: List, shape: List):
        self.cublets[cublet_name] = Cublet(image_position, shape)
