import imageio
import cv2 as cv
import numpy as np
import imutils
from images.series import Image


class CubeDetector:
    def __init__(self, face: Image):
        self.face = face
        self.face_corners = []
        self.template = imageio.imread("./outline-template.png")

    def detect_face(self):
        """This function detects a face of the cube and finds face corners

        """

        greyscale_img = self.face.get_greyscale()
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

            edge_img = cv.Canny(resized_img, 0, 100)
            template_match = cv.matchTemplate(edge_img, self.template, cv.TM_CCOEFF)

            (_, maxVal, _, maxLoc) = cv.minMaxLoc(template_match)

            if maxVal > best_fit_value:
                best_fit_value = maxVal
                best_fit_loc = np.array(maxLoc)
                best_fit_resize = resized_percentage

        # Calculate corners of face
        tl_corner = (best_fit_loc * best_fit_resize).astype(int)
        br_corner = ((best_fit_loc + self.template.shape) * best_fit_resize).astype(int)

        tr_corner = [tl_corner[0], br_corner[1]]
        bl_corner = [tl_corner[1], br_corner[0]]

        self.face_corners = [[tl_corner, tr_corner], [bl_corner, br_corner]]

    def face_to_cubies(self):
        """Split face into 9 seperate cubies
        """
        pass
