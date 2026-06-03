from enum import Enum, auto


class RunnerOptions(Enum):
    RUN = auto()
    GENERATE = auto()
    VISUALIZE = auto()
    VERSION = auto()

class e_University(int, Enum):
    NDSU = 0
    UND = 1
    MSUM = 2

class e_TeamType(int, Enum):
    UNDERGRADUATE = 0
    GRADUATE = 1
    ALUMNI = 2

