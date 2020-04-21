from state.constant import CubeletNames
from state.cube import detect_cube, Cube
from images.seriesManager import get_last_series
import matplotlib.pyplot as plt

series = get_last_series()
rep, cube = detect_cube(series)
print(Cube(rep).solve())


face_num = 5

fig, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9)) = plt.subplots(
    3, 3, sharex=True, sharey=True
)
ax1.imshow(cube[face_num].get_cubelet_image(CubeletNames.TL))
ax1.set_title(cube[face_num][CubeletNames.TL].color)
ax2.imshow(cube[face_num].get_cubelet_image(CubeletNames.TC))
ax2.set_title(cube[face_num][CubeletNames.TC].color)
ax3.imshow(cube[face_num].get_cubelet_image(CubeletNames.TR))
ax3.set_title(cube[face_num][CubeletNames.TR].color)

ax4.imshow(cube[face_num].get_cubelet_image(CubeletNames.ML))
ax4.set_title(cube[face_num][CubeletNames.ML].color)
ax5.imshow(cube[face_num].get_cubelet_image(CubeletNames.MC))
ax5.set_title(cube[face_num][CubeletNames.MC].color)
ax6.imshow(cube[face_num].get_cubelet_image(CubeletNames.MR))
ax6.set_title(cube[face_num][CubeletNames.MR].color)

ax7.imshow(cube[face_num].get_cubelet_image(CubeletNames.BL))
ax7.set_title(cube[face_num][CubeletNames.BL].color)
ax8.imshow(cube[face_num].get_cubelet_image(CubeletNames.BC))
ax8.set_title(cube[face_num][CubeletNames.BC].color)
ax9.imshow(cube[face_num].get_cubelet_image(CubeletNames.BR))
ax9.set_title(cube[face_num][CubeletNames.BR].color)

plt.show()
