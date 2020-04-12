import imageio
import imutils
import cv2 as cv
import numpy as np
from state.face import Face
from state.constant import CubletNames
from images.series import Image


class CubeDetector:
    def __init__(self, cublet_margin=2):
        self.cublet_margin = cublet_margin

        self.template = imageio.imread("./outline-template.png")

    def detect_face(self, face_state: Face):
        """This function detects a face of the cube and finds the top left face corner and face size

        """

        greyscale_img = face_state.face_image.get_greyscale()
        best_fit_value = 0
        best_fit_loc = (None, None)
        best_fit_resize = None

        for scale in np.linspace(0.1, 1.0, 30)[::-1]:
            resized_img = imutils.resize(
                greyscale_img, width=int(greyscale_img.shape[1] * scale)
            )
            resized_percentage = greyscale_img.shape[1] / float(resized_img.shape[1])

            # Break if image is smaller than template
            if (
                resized_img.shape[0] < self.template.shape[0]
                or resized_img.shape[1] < self.template.shape[1]
            ):
                break

            edge_img = cv.Canny(resized_img, 100, 200)
            template_match = cv.matchTemplate(edge_img, self.template, cv.TM_CCOEFF)

            (_, maxVal, _, maxLoc) = cv.minMaxLoc(template_match)

            if maxVal * resized_percentage > best_fit_value:
                best_fit_value = maxVal * resized_percentage
                best_fit_loc = np.array(maxLoc)
                best_fit_resize = resized_percentage

        face_state.face_shape = (
            np.array(self.template.shape) * best_fit_resize
        ).astype(int)
        face_state.face_location = (best_fit_loc[::-1] * best_fit_resize).astype(int)

    def detect_cublets(self, face_state: Face):
        """Split face into 9 seperate cubies
        
        """

        cublet_shape = ((face_state.face_shape - (6 * self.cublet_margin)) / 3).astype(
            "int"
        )

        for vert in range(3):
            for horiz in range(3):
                cublet_num = (vert * 3) + horiz

                cublet_location = (
                    face_state.face_location
                    + self.cublet_margin
                    + ((2 * self.cublet_margin + cublet_shape) * [vert, horiz])
                )

                face_state.set_cublet(
                    CubletNames.get_cublet_by_idx(cublet_num),
                    cublet_location,
                    cublet_shape,
                )
