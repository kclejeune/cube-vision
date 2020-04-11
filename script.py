from detectors.cubeDetector import CubeDetector
from images.seriesManager import get_last_series
from scipy.signal import correlate2d
import imageio
import numpy as np

series = get_last_series()
fd = CubeDetector(series["front"])
fd.detect_face()
