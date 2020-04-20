from images.series import Series
from state.detector import FaceDetector
from state.face import Face
from typing import List, Dict


class Cube:
    def __init__(self, series: Series):
        self.faces: List[Face] = [Face(series_image) for series_image in series]
        self.labeled_faces: Dict[str, Face] = {}

    def detect_cube(self):
        fd = FaceDetector()

        for face in self.faces:
            fd.detect_face(face)
            fd.detect_cublets_shape(face)
            fd.detect_cublets_color(face)

            self.labeled_faces[face.center_color] = face
