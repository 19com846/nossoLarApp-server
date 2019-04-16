from enum import Enum, auto, unique


@unique
class Role(Enum):
    STUDENT = auto()
    COLLABORATOR = auto()
    ADMIN = auto()

@unique
class Cycle(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FREE_COURSE = 0
