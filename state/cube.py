from images.series import Series
from state.detector import FaceDetector
from state.face import Face
from typing import List, Dict, Union

import kociemba

SIDES = ["U", "R", "F", "D", "L", "B"]
SOLVED = str_to_state("".join(side * 6 for side in SIDES))
MOVESET = SIDES + [side + "'" for side in SIDES]
print(MOVESET)


class Cube:
    def __init__(self, series: Series, state=SIDES):
        self.faces: List[Face] = [Face(series_image) for series_image in series]
        self.labeled_faces: Dict[str, Face] = {}

        self.state = str_to_state(state) if isinstance(state, str) else state

    def detect_cube(self):
        fd = FaceDetector()

        for face in self.faces:
            fd.detect_face(face)
            fd.detect_cublets_shape(face)
            fd.detect_cublets_color(face)

            self.labeled_faces[face.center_color] = face

    def solve(self, end_state: Dict[str, List[str]] = SOLVED) -> str:
        end_state = state_to_str(end_state)
        return kociemba.solve(state_to_str(self.state), patternstring=end_state).split(
            " "
        )

    def apply_sequence(self, sequence: List[str], start=None) -> Dict[str, List[str]]:
        if not start:
            start = self.state
        pass


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


def str_to_state(state: str) -> Dict[str, List[str]]:
    return {side: state[9 * i + j] for i, side in enumerate() for j in range(9)}


def state_to_str(state: Dict[str, List[str]]) -> str:
    return "".join("".join(state[side]) for side in SIDES)
