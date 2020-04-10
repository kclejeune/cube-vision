from faceDetector import FaceDetector
from seriesManager import get_last_series
from scipy.signal import correlate2d
import imageio
import numpy as np

series = get_last_series()
fd = FaceDetector(series["front"])
print(fd.detect())
