from scipy.signal import convolve2d
from seriesManager import get_last_series
import matplotlib.pyplot as plt
import imageio

img_series = get_last_series()
kernel = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
print(img_series.__getitem__("full").get_folder())
convolved = convolve2d(img_series["full"].image[:, :, 3], kernel, mode="same")
imageio.imsave("./new-image.png", convolved)
