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

plt.imshow(f.get_cublet_image("BL"))
plt.show()
