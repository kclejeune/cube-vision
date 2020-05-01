from images.series import Series
from state.detector import FaceDetector
from state.constant import Colors
from state.face import Face
from typing import List, Dict, Union
import numpy as np

import kociemba

# Define MACROS
SIDES = ["U", "R", "F", "D", "L", "B"]
MOVESET = SIDES + [side + "'" for side in SIDES]

# Converter Functions
def str_to_state(state: str) -> Dict[str, List[str]]:
    return {
        side: [[state[9 * i + (3 * y + x)] for x in range(3)] for y in range(3)]
        for i, side in enumerate(SIDES)
    }


def state_to_str(state: Dict[str, List[str]]) -> str:
    return "".join("".join(np.array(state[side]).flatten()) for side in SIDES)


# Define solved state
SOLVED = str_to_state("".join(side * 9 for side in SIDES))


class Cube:
    def __init__(self, state=SIDES):
        self.state = str_to_state(state) if isinstance(state, str) else state

    def solve(self, end_state: Dict[str, List[str]] = SOLVED) -> str:
        end_state = state_to_str(end_state)
        return kociemba.solve(state_to_str(self.state), patternstring=end_state).split(
            " "
        )

    def apply_sequence(self, sequence: List[str], start=None) -> Dict[str, List[str]]:
        if not start:
            start = self.state
        pass


def detect_cube(series: Series):
    fd = FaceDetector()
    faces: List[Face] = [Face(series_image) for series_image in series]
    encoded_faces: Dict[str, Face] = {}

    for face in faces:
        fd.detect_face(face)
        fd.detect_cubelets_shape(face)
        fd.detect_cubelets_color(face)

        encoded_faces[Colors.encode(face.center_color)] = face.get_encoded_face()

    if len(encoded_faces) != 6:
        raise Exception(
            "The cube that was found does not have 6 sides, Try better lighting."
        )

    return encoded_faces, faces


def detect_face(face: Face):
    fd = FaceDetector()

    fd.detect_face(face)
    fd.detect_cubelets_shape(face)
    fd.detect_cubelets_color(face)


def apply_turn(turn: str, state=SOLVED):
    if turn not in MOVESET:
        raise ValueError(f"Error: {turn} is not a valid turn.")

    if turn == "R":
        for i in range(start=2, stop=9, step=3):
            r = i // 3
            c = i % 3
            state["U"], state["B"][r][c], state["D"][r][c], state["F"][r][c] = (
                state["F"][r][c],
                state["U"][r][c],
                state["B"][9 - i + 1],
                state["D"][r][c],
            )
        state["R"] = rotate_clockwise(state["R"])
    elif turn == "L":
        for i in range(start=0, stop=9, step=3):
            r = i // 3
            c = i % 3
            state["U"], state["B"][r][c], state["D"][r][c], state["F"][r][c] = (
                state["B"][9 - i - 1],
                state["D"][r][c],
                state["F"][r][c],
                state["U"][r][c],
            )
            state["L"] = rotate_clockwise(state["L"])
    elif turn == "U":
        for i in range(3):
            r = i // 3
            c = i % 3
            state["R"][r][c], state["F"][r][c], state["L"][r][c], state["B"][r][c] = (
                state["B"][r][c],
                state["R"][r][c],
                state["F"][r][c],
                state["L"][r][c],
            )
        state["U"] = rotate_clockwise(state["U"])
    elif turn == "D":
        for i in range(5, 9):
            r = i // 3
            c = i % 3
            state["R"][r][c], state["F"][r][c], state["L"][r][c], state["B"][r][c] = (
                state["F"][r][c],
                state["L"][r][c],
                state["B"][r][c],
                state["R"][r][c],
            )
        state["D"] = rotate_clockwise(state["D"])
    elif turn == "F":
        for i in range(start=0, stop=9, step=3):
            r = i // 3
            c = i % 3
            state["R"][r][c], state["D"][r][c], state["L"][r][c], state["U"][r][c] = (
                state["U"][r][c],
                state["R"][r][c],
                state["D"][r][c],
                state["L"][r][c],
            )
        state["F"] = rotate_clockwise(state["F"])
    elif turn == "B":
        pass


def rotate_clockwise(arr):
    return zip(*arr[::-1])
