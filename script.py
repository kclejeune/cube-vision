from detectors.cubeDetector import CubeDetector
from state.face import Face
from images.seriesManager import get_last_series
from scipy.signal import correlate2d
import imageio
import numpy as np
import matplotlib.pyplot as plt

series = get_last_series()
fd = CubeDetector()
f = Face(series["front"])

fd.detect_face(f)
fd.detect_cubies(f)

cropped_image = f.face_image.image[
    f.face_location[0] : f.face_location[0] + f.face_shape[0],
    f.face_location[1] : f.face_location[1] + f.face_shape[1],
]


plt.imshow(cropped_image)
plt.imshow(f.get_cublet_image("BL"))
plt.show()
