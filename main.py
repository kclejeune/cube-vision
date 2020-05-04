from state.constant import CubeletNames
from state.cube import detect_cube, detect_face, Cube
from state.face import Face

from images.series import Image
from images.seriesManager import get_last_series, get_series

import matplotlib.pyplot as plt
from extensions.camera import Camera
from cv2 import cv2
import argparse


def run(args):
    if args.live and args.series != None:
        raise Exception("You can't use the live feature and request a series")
    elif args.live:
        run_camera(args)
    else:
        if args.series != None:
            series = get_series(args.series)
        else:
            series = get_last_series()

        rep, cube = detect_cube(series)

        if len(rep) == 6:
            print(Cube(rep).solve())
        else:
            print("The cube that was found does not have 6 sides, Try better lighting.")

        if not args.noimg:
            for face in cube[:-1]:
                show_face(face)
                plt.show(block=False)
            show_face(cube[-1])
            plt.show()


def run_camera(args):
    cam = Camera()
    count = 0
    while cam.thread.isAlive:
        frame = cam.frame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face = Face(Image(frame))
        detect_face(face)

        if not args.noimg:
            show_face(face)
            plt.show(block=False)
            plt.pause(2)
            plt.close()

        key = cv2.waitKey(20)
        if key == 27:
            cam.end()
            break


def show_face(face):
    fig, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9)) = plt.subplots(
        3, 3, sharex=True, sharey=True
    )

    ax1.imshow(face.get_cubelet_image(CubeletNames.TL))
    ax1.set_title(face[CubeletNames.TL].color)
    ax2.imshow(face.get_cubelet_image(CubeletNames.TC))
    ax2.set_title(face[CubeletNames.TC].color)
    ax3.imshow(face.get_cubelet_image(CubeletNames.TR))
    ax3.set_title(face[CubeletNames.TR].color)

    ax4.imshow(face.get_cubelet_image(CubeletNames.ML))
    ax4.set_title(face[CubeletNames.ML].color)
    ax5.imshow(face.get_cubelet_image(CubeletNames.MC))
    ax5.set_title(face[CubeletNames.MC].color)
    ax6.imshow(face.get_cubelet_image(CubeletNames.MR))
    ax6.set_title(face[CubeletNames.MR].color)

    ax7.imshow(face.get_cubelet_image(CubeletNames.BL))
    ax7.set_title(face[CubeletNames.BL].color)
    ax8.imshow(face.get_cubelet_image(CubeletNames.BC))
    ax8.set_title(face[CubeletNames.BC].color)
    ax9.imshow(face.get_cubelet_image(CubeletNames.BR))
    ax9.set_title(face[CubeletNames.BR].color)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Cube Vision")
    parser.add_argument("-s", "--series", help="specify series number", type=int)
    parser.add_argument(
        "-n", "--noimg", help="hide cubelet images", action="store_true"
    )
    parser.add_argument("-l", "--live", help="live cube detection", action="store_true")
    args = parser.parse_args()

    run(args)
