
from seriesManager import get_last_series
import imageio
import cv2 as cv
import numpy as np
import imutils
from series import Image


class FaceDetector():
    def __init__(self, face: Image):
        self.face = face
        self.template = imageio.imread("./outline-template.png")

    def detect(self):
        """This function detects a face of the cube
        
        Returns:
            array of the top left and bottom right corners of the matched area
        """
        greyscale_img = self.face.get_greyscale()
        best_fit_value = 0
        best_fit_loc = (None, None)
        best_fit_resize = None

        for scale in np.linspace(0.1, 1.0, 30)[::-1]:
            resized_img = imutils.resize(greyscale_img, width = int(greyscale_img.shape[1] * scale))
            resized_percentage = greyscale_img.shape[1] / float(resized_img.shape[1])

            # Break if image is smaller than template
            if resized_img.shape[0] < self.template.shape[0] or resized_img.shape[1] < self.template.shape[1]:
                break

            edge_img = cv.Canny(resized_img, 0, 100)
            template_match = cv.matchTemplate(edge_img, self.template, cv.TM_CCOEFF)

            (_, maxVal, _, maxLoc) = cv.minMaxLoc(template_match)

            if maxVal > best_fit_value:
                best_fit_value = maxVal
                best_fit_loc = maxLoc
                best_fit_resize =  resized_percentage


        tl_corner = [int(best_fit_loc[0] * best_fit_resize), int(best_fit_loc[1] * best_fit_resize)]
        br_corner = [int((best_fit_loc[0] + self.template.shape[0]) * best_fit_resize), int((best_fit_loc[1] + self.template.shape[1]) * best_fit_resize)]
        
        return (tl_corner, br_corner)