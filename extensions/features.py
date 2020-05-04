import numpy as np
from cv2 import cv2
import imageio
from matplotlib import pyplot as plt
from images.seriesManager import get_series

img1 = imageio.imread("./feature.jpg")  # queryImage
img2 = get_series(2)[4].convert_to_greyscale()

# Initiate SIFT detector
orb = cv2.ORB_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors.
matches = bf.match(des1, des2)

# Sort them in the order of their distance.
matches = sorted(matches, key=lambda x: x.distance)

# Draw first 10 matches.
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[0:50], None, flags=2)

plt.imshow(img3), plt.show()
