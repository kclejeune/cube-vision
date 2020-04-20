from state.constant import CubeletNames
from state.cube import detect_cube
from images.seriesManager import get_last_series
import matplotlib.pyplot as plt

series = get_last_series()
cube = detect_cube(series)
print(cube)


# This looks so yummy
# print([cubelet.color for cubelet in cube.faces[0]])
# print([cubelet.color for cubelet in cube.faces[1]])
# print([cubelet.color for cubelet in cube.faces[2]])
# print([cubelet.color for cubelet in cube.faces[3]])
# print([cubelet.color for cubelet in cube.faces[4]])
# print([cubelet.color for cubelet in cube.faces[5]])


# fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, sharex=True, sharey=True)
# ax1.imshow(cube.faces[0].get_face_image())
# ax2.imshow(cube.faces[1].get_face_image())
# ax3.imshow(cube.faces[2].get_face_image())
# ax4.imshow(cube.faces[3].get_face_image())
# ax5.imshow(cube.faces[4].get_face_image())
# ax6.imshow(cube.faces[5].get_face_image())
# plt.show()
