from enum import Enum


# ----------------------------------------------------------
class PercentUnits(Enum):
    PERCENT = 0


# ----------------------------------------------------------
class TimeUnits(Enum):
    SECONDS = 0
    SEC = 0
    MSEC = 1


# ----------------------------------------------------------
class RotationUnits(Enum):
    DEG = 0


# ----------------------------------------------------------
class VelocityUnits(Enum):
    PCT = 0


# ----------------------------------------------------------
class DistanceUnits(Enum):
    MM = 0
    IN = 1


# ----------------------------------------------------------
class DirectionType(Enum):
    FORWARD = 1
    REVERSE = -1


# ----------------------------------------------------------
class TurnType(Enum):
    LEFT = -1
    RIGHT = 1


# ----------------------------------------------------------
class MagnetType(Enum):
    BOOST = "boost"
    DROP = "drop"


class ColorType(Enum):
    BLACK = 0
    NONE = 0
    RED = 1
    GREEN = 2
    BLUE = 3


class PenPositionType(Enum):
    UP = 0
    DOWN = 1


class PenWidthType(Enum):
    EXTRA_THIN = 0
    THIN = 1
    MEDIUM = 3
    WIDE = 4
    EXTRA_WIDE = 5


class PositionType(Enum):
    X = "X"
    Y = "Y"


# ----------------------------------------------------------
class LocatableObject(Enum):
    MINERALS = "minerals"
    ENEMY = "enemy"
    BASE = "base"
    OBSTACLE = "obstacle"
    HAZARD = "hazard"
    ROVER = "rover"


class DetectableObject(Enum):
    MINERALS = "minerals"
    ENEMY = "enemy"
    BASE = "base"
    OBSTACLE = "obstacle"
    HAZARD = "hazard"


class PickupObject(Enum):
    MINERALS = "minerals"


class AbsorbObject(Enum):
    ENEMY = "enemy"


class SmellableObject(Enum):
    MINERALS = "minerals"
    ENEMY = "enemy"


class SeeableAngleObject(Enum):
    MINERALS = "minerals"
    ENEMY = "enemy"
    BASE = "base"


# ----------------------------------------------------------
# globals
#
PERCENT = PercentUnits.PERCENT
FORWARD = DirectionType.FORWARD
REVERSE = DirectionType.REVERSE
LEFT = TurnType.LEFT
RIGHT = TurnType.RIGHT
DEGREES = RotationUnits.DEG
SECONDS = TimeUnits.SECONDS
SEC = TimeUnits.SEC
MSEC = TimeUnits.MSEC
INCHES = DistanceUnits.IN
MM = DistanceUnits.MM
BOOST = MagnetType.BOOST
DROP = MagnetType.DROP
BLACK = ColorType.BLACK
NONE = ColorType.NONE
RED = ColorType.RED
GREEN = ColorType.GREEN
BLUE = ColorType.BLUE
UP = PenPositionType.UP
DOWN = PenPositionType.DOWN
X = PositionType.X
Y = PositionType.Y
EXTRA_THIN = PenWidthType.EXTRA_THIN
THIN = PenWidthType.THIN
MEDIUM = PenWidthType.MEDIUM
WIDE = PenWidthType.WIDE
EXTRA_WIDE = PenWidthType.EXTRA_WIDE

MINERALS = LocatableObject.MINERALS
ENEMY = LocatableObject.ENEMY
BASE = LocatableObject.BASE
OBSTACLE = LocatableObject.OBSTACLE
HAZARD = LocatableObject.HAZARD
ROVER = LocatableObject.ROVER

__all__ = [
    "PercentUnits",
    "TimeUnits",
    "RotationUnits",
    "VelocityUnits",
    "DistanceUnits",
    "DirectionType",
    "TurnType",
    "MagnetType",
    "ColorType",
    "PenPositionType",
    "PenWidthType",
    "PositionType",
    "SmellableObject",
    "DetectableObject",
    "PickupObject",
    "AbsorbObject",
    "SeeableAngleObject",
    "LocatableObject",
    "PERCENT",
    "FORWARD",
    "REVERSE",
    "LEFT",
    "RIGHT",
    "DEGREES",
    "SEC",
    "SECONDS",
    "MSEC",
    "INCHES",
    "MM",
    "BOOST",
    "DROP",
    "BLACK",
    "NONE",
    "RED",
    "GREEN",
    "BLUE",
    "UP",
    "DOWN",
    "X",
    "Y",
    "ROVER",
    "MINERALS",
    "ENEMY",
    "BASE",
    "OBSTACLE",
    "HAZARD",
    "EXTRA_THIN",
    "THIN",
    "MEDIUM",
    "WIDE",
    "EXTRA_WIDE",
]
