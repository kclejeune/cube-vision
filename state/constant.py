from typing import List


class Colors:
    WHITE: str = "white"
    YELLOW: str = "yellow"
    RED: str = "red"
    ORANGE: str = "orange"
    BLUE: str = "blue"
    GREEN: str = "green"


class CubletNames:
    TL: str = "top-left"
    TC: str = "top-center"
    TR: str = "top-right"

    ML: str = "middle-left"
    MC: str = "middle-center"
    MR = "middle-right"

    BL: str = "bottom-left"
    BC: str = "bottom-center"
    BR: str = "bottom-right"

    @classmethod
    def get_cublet_order(cls) -> List[str]:
        return [cls.TL, cls.TC, cls.TR, cls.ML, cls.MC, cls.MR, cls.BL, cls.BC, cls.BR]

    @classmethod
    def get_cublet_by_idx(cls, idx) -> str:
        return cls.get_cublet_order()[idx]
