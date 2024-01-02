import asyncio
import inspect
from enum import Enum


# Mock vex js api
class vexcode_api:
    pass


##########
# Enums #
#########
from enum import Enum


# ----------------------------------------------------------
class PercentUnits(Enum):
    """
    Enumeration for percent units.

    This enum class is used to represent different types of percent units. 
    Currently, it only includes the 'PERCENT' unit.

    Attributes:
        PERCENT (int): Represents the standard percentage unit.
    """
    PERCENT = 0


# ----------------------------------------------------------
class TimeUnits(Enum):
    """
    Enumeration for time units.

    This enum class is used to define different units of time for use in 
    various applications. It includes options for seconds and milliseconds.

    Attributes:
        SECONDS (int): Represents time in seconds. Alias is 'SEC'.
        SEC (int): Alias for representing time in seconds. Same as 'SECONDS'.
        MSEC (int): Represents time in milliseconds.
    """
    SECONDS = 0
    SEC = 0
    MSEC = 1


# ----------------------------------------------------------
class RotationUnits(Enum):
    """
    Enumeration for rotation units.

    This enum class is used for specifying the unit of rotation measurement. 
    It currently includes an option for degrees.

    Attributes:
        DEG (int): Represents the rotation unit in degrees.
    """
    DEG = 0


# ----------------------------------------------------------
class VelocityUnits(Enum):
    """
    Enumeration for velocity units.

    This enum class is designed for defining different units of velocity 
    measurement. Currently, it includes an option for percentage.

    Attributes:
        PCT (int): Represents the velocity unit as a percentage.
    """
    PCT = 0


# ----------------------------------------------------------
class DistanceUnits(Enum):
    """
    Enumeration for distance units.

    This enum class defines different units of distance measurement used in
    various contexts. It includes options for millimeters and inches.

    Attributes:
        MM (int): Represents distance in millimeters.
        IN (int): Represents distance in inches.
    """
    MM = 0
    IN = 1


# ----------------------------------------------------------
class DirectionType(Enum):
    """
    Enumeration for direction types.

    This enum class is utilized to define direction types for various control 
    mechanisms or movement instructions. It includes options for forward and reverse directions.

    Attributes:
        FORWARD (int): Represents the forward direction, denoted by 1.
        REVERSE (int): Represents the reverse direction, denoted by -1.
    """
    FORWARD = 1
    REVERSE = -1


# ----------------------------------------------------------
class TurnType(Enum):
    """
    Enumeration for turn types.

    This enum class is used for defining the direction of a turn. It supports 
    two types of turns: left and right.

    Attributes:
        LEFT (int): Represents a turn to the left, denoted by -1.
        RIGHT (int): Represents a turn to the right, denoted by 1.
    """
    LEFT = -1
    RIGHT = 1


# ----------------------------------------------------------
class MagnetType(Enum):
    """
    Enumeration for magnet types.

    This enum class defines the types of magnets used in certain applications.
    It includes options for both 'boost' and 'drop' types.

    Attributes:
        BOOST (str): Represents a magnet type designed to boost or increase something.
        DROP (str): Represents a magnet type designed to drop or decrease something.
    """
    BOOST = "boost"
    DROP = "drop"


class ColorType(Enum):
    """
    Enumeration for color types.

    This enum class is used for defining basic color types. It includes black,
    red, green, blue, and a special 'none' type.

    Attributes:
        BLACK (int): Represents the color black. Same value as 'NONE'.
        NONE (int): Represents no color. Same value as 'BLACK'.
        RED (int): Represents the color red.
        GREEN (int): Represents the color green.
        BLUE (int): Represents the color blue.
    """
    BLACK = 0
    NONE = 0
    RED = 1
    GREEN = 2
    BLUE = 3


class PenPositionType(Enum):
    """
    Enumeration for pen position types.

    This enum class is used for specifying the position of a pen in drawing applications.
    It includes options for the pen being up or down.

    Attributes:
        UP (int): Represents the pen position being up (not in contact with the drawing surface).
        DOWN (int): Represents the pen position being down (in contact with the drawing surface).
    """
    UP = 0
    DOWN = 1


class PenWidthType(Enum):
    """
    Enumeration for pen width types.

    This enum class defines different widths for a pen stroke. It ranges from 
    extra thin to extra wide, accommodating various drawing styles.

    Attributes:
        EXTRA_THIN (int): Represents an extra thin pen stroke.
        THIN (int): Represents a thin pen stroke.
        MEDIUM (int): Represents a medium-width pen stroke.
        WIDE (int): Represents a wide pen stroke.
        EXTRA_WIDE (int): Represents an extra wide pen stroke.
    """
    EXTRA_THIN = 0
    THIN = 1
    MEDIUM = 3
    WIDE = 4
    EXTRA_WIDE = 5


class PositionType(Enum):
    """
    Enumeration for axis position types.

    This enum class is used for specifying axis positions in a two-dimensional space.
    It includes options for 'X' (horizontal axis) and 'Y' (vertical axis) positions.

    Attributes:
        X (str): Represents the X-axis (horizontal) position.
        Y (str): Represents the Y-axis (vertical) position.
    """
    X = "X"
    Y = "Y"


# ----------------------------------------------------------
class LocatableObject(Enum):
    """
    Enumeration for locatable objects.

    This enum class defines various objects that can be located within a given environment. 
    It includes minerals, enemies, bases, obstacles, hazards, and rovers.

    Attributes:
        MINERALS (str): Represents minerals that can be located.
        ENEMY (str): Represents enemies that can be located.
        BASE (str): Represents bases that can be located.
        OBSTACLE (str): Represents obstacles that can be located.
        HAZARD (str): Represents hazards that can be located.
        ROVER (str): Represents rovers that can be located.
    """
    MINERALS = "minerals"
    ENEMY = "enemy"
    BASE = "base"
    OBSTACLE = "obstacle"
    HAZARD = "hazard"
    ROVER = "rover"


class DetectableObject(Enum):
    """
    Enumeration for detectable objects.

    This enum class defines different objects that can be detected, excluding the 'rover'. 
    It includes minerals, enemies, bases, obstacles, and hazards.

    Attributes:
        MINERALS (str): Represents detectable minerals.
        ENEMY (str): Represents detectable enemies.
        BASE (str): Represents detectable bases.
        OBSTACLE (str): Represents detectable obstacles.
        HAZARD (str): Represents detectable hazards.
    """
    MINERALS = "minerals"
    ENEMY = "enemy"
    BASE = "base"
    OBSTACLE = "obstacle"
    HAZARD = "hazard"


class PickupObject(Enum):
    """
    Enumeration for objects that can be picked up.

    This enum class is specifically for identifying objects that can be physically picked up. 
    Currently, it only includes minerals.

    Attributes:
        MINERALS (str): Represents minerals that can be picked up.
    """
    MINERALS = "minerals"


class AbsorbObject(Enum):
    """
    Enumeration for objects that can be absorbed.

    This enum class defines objects that are capable of being absorbed. 
    As of now, it only includes enemies.

    Attributes:
        ENEMY (str): Represents enemies that can be absorbed.
    """
    ENEMY = "enemy"



class SmellableObject(Enum):
    """
    Enumeration for objects that can be smelled.

    This enum class lists objects that have a distinct smell and can be detected through olfactory means. 
    It includes both minerals and enemies.

    Attributes:
        MINERALS (str): Represents minerals that can be smelled.
        ENEMY (str): Represents enemies that can be smelled.
    """
    MINERALS = "minerals"
    ENEMY = "enemy"



class SeeableAngleObject(Enum):
    """
    Enumeration for objects visible from certain angles.

    This enum class specifies objects that can be seen from specific angles. 
    It includes minerals, enemies, and bases.

    Attributes:
        MINERALS (str): Represents minerals visible from certain angles.
        ENEMY (str): Represents enemies visible from certain angles.
        BASE (str): Represents bases visible from certain angles.
    """
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

##########
# Events #
##########


def get_Task_func():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None
    return loop.create_task if loop and loop.is_running() else asyncio.run


async def call_callback(cb):
    if callable(cb):
        res = cb()  # here's result of regular func or awaitable
        if inspect.isawaitable(res):
            res = await res  # await if awaitable
        return res  # return final result
    else:
        raise ValueError("cb is not callable")


async def call_callback_value(cb, value):
    if callable(cb):
        res = cb(value)  # here's result of regular func or awaitable
        if inspect.isawaitable(res):
            res = await res  # await if awaitable
        return res  # return final result
    else:
        raise ValueError("cb is not callable")


async def call_callbacks(cbs):
    func = get_Task_func()
    res = [func(call_callback(cb)) for cb in cbs]
    await asyncio.gather(*res)


class Event:
    def __init__(self):
        self._callbacks = []

    def __call__(self, callback):
        self._callbacks.append(callback)

    def broadcast(self):
        func = get_Task_func()
        func(call_callbacks(self._callbacks))

    async def broadcast_and_wait(self):
        func = get_Task_func()
        await func(call_callbacks(self._callbacks))


class BrainEvents:
    def __init__(self):
        self._callbacks = []

    def add_listener(self, callback):
        if not callable(callback):
            raise ValueError("callback is not callable")
        self._callbacks.append(callback)

    def trigger_event(self, event_type):
        func = get_Task_func()

        for cb in self._callbacks:
            func(call_callback_value(cb, event_type))


brain_events = BrainEvents()


class SensorEvents:
    def __init__(self):
        self._callbacks = [[] for x in range(23)]

    def add_listener(self, port, callback):
        if callable(callback):
            self._callbacks[port].append(callback)
        else:
            raise ValueError("callback is not callable")

    def trigger_event(self, port, value):
        func = get_Task_func()

        for cb in self._callbacks[port]:
            func(call_callback_value(cb, value))


sensor_events = SensorEvents()


###########
# DEVICES #
###########


def constrainValue(val, min_val, max_val):
    return min(max_val, max(min_val, val))


class _VexCodeDevice:
    def __init__(self, name, port):
        self._device_name = name
        self._device_port = port


class Drivetrain(_VexCodeDevice):
    def __init__(self, name, port):
        super().__init__(name, port)
        self.timeout = 0

    def drive(self, direction):
        if not isinstance(direction, DirectionType):
            raise TypeError("direction must be a DirectionType")
        vexcode_api.drivetrainDrive(self._device_port, direction.value)

    async def drive_for(self, direction, amount, units, wait=True):
        if not isinstance(direction, DirectionType):
            raise TypeError("direction must be a DirectionType")
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be a int or float")
        if not isinstance(units, DistanceUnits):
            raise TypeError("units must be a DistanceUnits")
        if not isinstance(wait, bool):
            raise TypeError("wait must be a boolean")
        if units == INCHES:
            amount *= 25.4
        await vexcode_api.drivetrainDriveFor(
            self._device_port, direction.value, amount, wait, self.timeout
        )

    async def drive_to(self, object, wait=True):
        if (
            not isinstance(object, LocatableObject)
            and object.name in DetectableObject.__members__
        ):
            raise TypeError("object must be a DetectableObject")
        if not isinstance(wait, bool):
            raise TypeError("wait must be a boolean")
        await vexcode_api.drivetrainDriveTo(
            self._device_port, object.value, wait, self.timeout
        )

    def turn(self, direction):
        if not isinstance(direction, TurnType):
            raise TypeError("direction must be a TurnType")
        vexcode_api.drivetrainTurn(self._device_port, direction.value)

    async def turn_for(self, direction, amount, units, wait=True):
        if not isinstance(direction, TurnType):
            raise TypeError("direction must be a TurnType")
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be a int or float")
        if not isinstance(units, RotationUnits):
            raise TypeError("units must be a RotationUnits")
        if not isinstance(wait, bool):
            raise TypeError("wait must be a boolean")
        await vexcode_api.drivetrainTurnFor(
            self._device_port, direction.value, amount, wait, self.timeout
        )

    def swing(self, direction, turnradius, turnunits):
        if not isinstance(direction, TurnType):
            raise TypeError("direction must be a TurnType")
        if not isinstance(turnradius, (int, float)):
            raise TypeError("turnradius must be a int or float")
        if not isinstance(turnunits, DistanceUnits):
            raise TypeError("turnunits must be a DistanceUnits")
        if turnunits == INCHES:
            turnradius *= 25.4
        vexcode_api.drivetrainSwing(self._device_port, direction.value, turnradius)

    async def swing_for(
        self, direction, amount, units, turnradius, turnunits, wait=True
    ):
        if not isinstance(direction, TurnType):
            raise TypeError("direction must be a TurnType")
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be a int or float")
        if not isinstance(units, RotationUnits):
            raise TypeError("units must be a RotationUnits")
        if not isinstance(turnradius, (int, float)):
            raise TypeError("turnradius must be a int or float")
        if not isinstance(turnunits, DistanceUnits):
            raise TypeError("turnunits must be a DistanceUnits")
        if not isinstance(wait, bool):
            raise TypeError("wait must be a boolean")
        if turnunits == INCHES:
            turnradius *= 25.4
        await vexcode_api.drivetrainSwingFor(
            self._device_port, direction.value, amount, turnradius, wait, self.timeout
        )

    async def turn_to(self, object, wait=True):
        if (
            not isinstance(object, LocatableObject)
            and object.name in DetectableObject.__members__
        ):
            raise TypeError("object must be a DetectableObject")
        if not isinstance(wait, bool):
            raise TypeError("wait must be a boolean")
        await vexcode_api.drivetrainTurnTo(
            self._device_port, object.value, wait, self.timeout
        )

    async def turn_to_heading(self, heading, units, wait=True):
        if not isinstance(heading, (int, float)):
            raise TypeError("heading must be a int or float")
        if not isinstance(units, RotationUnits):
            raise TypeError("units must be a RotationUnits")
        if not isinstance(wait, bool):
            raise TypeError("wait must be a boolean")
        heading = heading % 360
        await vexcode_api.drivetrainTurnToHeading(
            self._device_port, heading, wait, self.timeout
        )

    async def turn_to_rotation(self, rotation, units, wait=True):
        if not isinstance(rotation, (int, float)):
            raise TypeError("rotation must be a int or float")
        if not isinstance(units, RotationUnits):
            raise TypeError("units must be a RotationUnits")
        if not isinstance(wait, bool):
            raise TypeError("wait must be a boolean")
        await vexcode_api.drivetrainTurnToRotation(
            self._device_port, rotation, wait, self.timeout
        )

    async def go_to(self, object, wait=True):
        if (
            not isinstance(object, LocatableObject)
            and object.name in DetectableObject.__members__
        ):
            raise TypeError("object must be a DetectableObject")
        if not isinstance(wait, bool):
            raise TypeError("wait must be a boolean")
        await vexcode_api.drivetrainGoTo(
            self._device_port, object.value, wait, self.timeout
        )

    def stop(self):
        vexcode_api.drivetrainStop(self._device_port)

    def set_drive_velocity(self, velocity, units):
        if not isinstance(velocity, (int, float)):
            raise TypeError("velocity must be a int or float")
        if not isinstance(units, PercentUnits):
            raise TypeError("units must be a PercentUnits")
        velocity = constrainValue(velocity, -100, 100)
        vexcode_api.drivetrainSetDriveVelocity(self._device_port, velocity)

    def set_turn_velocity(self, velocity, units):
        if not isinstance(velocity, (int, float)):
            raise TypeError("velocity must be a int or float")
        if not isinstance(units, PercentUnits):
            raise TypeError("units must be a PercentUnits")
        velocity = constrainValue(velocity, -100, 100)
        vexcode_api.drivetrainSetTurnVelocity(self._device_port, velocity)

    async def set_heading(self, heading, units):
        if not isinstance(heading, (int, float)):
            raise TypeError("heading must be a int or float")
        if not isinstance(units, RotationUnits):
            raise TypeError("units must be a RotationUnits")
        heading = heading % 360
        await vexcode_api.drivetrainSetDriveHeading(self._device_port, heading)
        await wait(0.02, SECONDS)

    async def set_rotation(self, rotation, units):
        if not isinstance(rotation, (int, float)):
            raise TypeError("rotation must be a int or float")
        if not isinstance(units, RotationUnits):
            raise TypeError("units must be a RotationUnits")
        await vexcode_api.drivetrainSetDriveRotation(self._device_port, rotation)
        await wait(0.02, SECONDS)

    async def set_timeout(self, timeout, units):
        if not isinstance(timeout, (int, float)):
            raise TypeError("timeout must be an int or float")
        if not isinstance(units, TimeUnits):
            raise TypeError("units must be a TimeUnits")
        if units == SECONDS:
            timeout *= 1000
        self.timeout = timeout

    def is_done(self):
        return vexcode_api.drivetrainGetDriveIsDone(self._device_port)

    def is_moving(self):
        return vexcode_api.drivetrainGetDriveIsMoving(self._device_port)

    def heading(self, units):
        if not isinstance(units, RotationUnits):
            raise TypeError("units must be a RotationUnits")
        return vexcode_api.drivetrainGetDriveHeading(self._device_port)

    def rotation(self, units):
        if not isinstance(units, RotationUnits):
            raise TypeError("units must be a RotationUnits")
        return vexcode_api.drivetrainGetDriveRotation(self._device_port)


class Motor(_VexCodeDevice):
    async def spin(self, direction):
        if not isinstance(direction, DirectionType):
            raise TypeError("direction must be a DirectionType")
        pass

    async def spin_for(self, direction, amount, units, wait=True):
        if not isinstance(direction, DirectionType):
            raise TypeError("direction must be a DirectionType")
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be a int or float")
        if not isinstance(units, DistanceUnits):
            raise TypeError("units must be a RotationUnits")
        if not isinstance(wait, bool):
            raise TypeError("wait must be a boolean")
        pass

    async def spin_to_position(self, position, units, wait=True):
        if not isinstance(position, (int, float)):
            raise TypeError("position must be a int or float")
        if not isinstance(units, RotationUnits):
            raise TypeError("units must be a RotationUnits")
        if not isinstance(wait, bool):
            raise TypeError("wait must be a boolean")
        pass

    async def stop(self):
        pass

    async def set_position(self, position, units):
        if not isinstance(position, (int, float)):
            raise TypeError("position must be a int or float")
        if not isinstance(units, RotationUnits):
            raise TypeError("units must be a RotationUnits")
        pass

    async def set_velocity(self, velocity, units):
        if not isinstance(velocity, (int, float)):
            raise TypeError("velocity must be a int or float")
        if not isinstance(units, PercentUnits):
            raise TypeError("units must be a PercentUnits")
        velocity = constrainValue(velocity, -100, 100)
        pass

    # async def set_timeout(self, timeout, units):
    #     pass

    def is_done(self):
        pass

    def is_moving(self):
        pass

    def position(self, units):
        if not isinstance(units, RotationUnits):
            raise TypeError("units must be a RotationUnits")
        pass


class Electromagnet(_VexCodeDevice):
    def energize(self, mode):
        if not isinstance(mode, MagnetType):
            raise TypeError("mode must be a MagnetType")
        vexcode_api.magnetEnergize(self._device_port, mode.value)


class Brain:
    def __init__(self):
        self._timer_events = []
        func = get_Task_func()
        func(self._check_events_loop())
        pass

    def print(self, *objects, precision=0):
        # make sure precision is a number
        if not precision or not isinstance(precision, (int, float, complex)):
            precision = 0
        # default precision
        if precision == -1:
            precision = 6
        # limit 0 <= precision <= 9
        precision = constrainValue(precision, 0, 9)
        number_template = "{{:.{:.0f}f}}".format(precision)

        # create a function to convert objects to strings
        def obj_to_str(obj):
            if isinstance(obj, (int, float, complex)) and not isinstance(obj, (bool)):
                return number_template.format(obj)
            else:
                return "{}".format(obj)

        # build a string for each object pased to the method
        output = " ".join(map(obj_to_str, objects))

        # actually print the text to the vexcode console
        vexcode_api.sendPrintText(output)

    def clear(self):
        vexcode_api.sendPrintClearLines()

    def new_line(self):
        vexcode_api.sendPrintNewLine()

    def set_print_color(self, color):
        if not isinstance(color, ColorType):
            raise TypeError("color must be a ColorType")
        vexcode_api.sendPrintSetColor(color.name)

    def timer_reset(self):
        vexcode_api.resetTimer()

    def timer_time(self, units):
        if not isinstance(units, TimeUnits):
            raise TypeError("units must be a TimeUnits")
        timerms = vexcode_api.getTimer()
        if units is SECONDS:
            return timerms / 1000
        return timerms

    def timer_event(self, callback, time):
        if not callable(callback):
            raise ValueError("callback is not callable")
        if not isinstance(time, (int, float)):
            raise TypeError("time must be a int or float")
        self._timer_events.append(
            {"timems": time, "has_triggered": False, "callback": callback}
        )

    def _check_events(self):
        if len(self._timer_events) > 0:
            timerms = vexcode_api.getTimer()
            func = get_Task_func()
            for event in self._timer_events:
                if not event["has_triggered"]:
                    if event["timems"] <= timerms:
                        event["has_triggered"] = True
                        func(call_callback(event["callback"]))

    async def _check_events_loop(self):
        while True:
            await asyncio.sleep(0.01)
            self._check_events()


class Rover(_VexCodeDevice):
    def __init__(self, name, port):
        super().__init__(name, port)
        self._attack_events = []
        self._level_events = []
        brain_events.add_listener(self._on_brain_event)
        pass

    async def pickup(self, object):
        if (
            not isinstance(object, LocatableObject)
            and object.name in PickupObject.__members__
        ):
            raise TypeError("object must be an PickupObject")
        await vexcode_api.pickup(self._device_port, object.value)

    async def drop(self, object):
        if (
            not isinstance(object, LocatableObject)
            and object.name in PickupObject.__members__
        ):
            raise TypeError("object must be an PickupObject")
        await vexcode_api.drop(self._device_port, object.value)

    async def use(self, object):
        if (
            not isinstance(object, LocatableObject)
            and object.name in PickupObject.__members__
        ):
            raise TypeError("object must be an PickupObject")
        await vexcode_api.use(self._device_port, object.value)

    async def absorb_radiation(self, target):
        if (
            not isinstance(target, LocatableObject)
            and target.name in AbsorbObject.__members__
        ):
            raise TypeError("target must be an AbsorbObject")
        await vexcode_api.absorb_radiation(self._device_port, target.value)

    async def standby(self, percent):
        if not isinstance(percent, (int, float)):
            raise TypeError("percent must be a number")
        await vexcode_api.standby(self._device_port, percent)

    def on_under_attack(self, callback):
        self._attack_events.append(callback)

    def on_level_up(self, callback):
        self._level_events.append(callback)

    def _on_under_attack(self):
        func = get_Task_func()
        for cb in self._attack_events:
            func(call_callback(cb))

    def _on_level_up(self):
        func = get_Task_func()
        for cb in self._level_events:
            func(call_callback(cb))

    def _on_brain_event(self, event_type):
        if event_type == "attack":
            self._on_under_attack()
        elif event_type == "level":
            self._on_level_up()
        else:
            raise TypeError("unknown brain event type")

    def battery(self):
        return vexcode_api.battery(self._device_port)

    def minerals_stored(self):
        return vexcode_api.mineralsStored(self._device_port)

    def level(self):
        return vexcode_api.level(self._device_port)

    def exp(self):
        return vexcode_api.exp(self._device_port)

    async def enemy_level(self):
        return await vexcode_api.enemyLevel(self._device_port)

    async def enemy_radiation(self):
        return await vexcode_api.enemyRadiation(self._device_port)

    def storage_capacity(self):
        return vexcode_api.storageCapacity(self._device_port)

    def under_attack(self):
        return vexcode_api.underAttack(self._device_port)

    async def detects(self, object):
        if (
            not isinstance(object, LocatableObject)
            and object.name in SmellableObject.__members__
        ):
            raise TypeError("object must be a SmellableObject")
        result = await vexcode_api.detects(self._device_port, object.value)
        return result

    async def sees(self, object):
        if (
            not isinstance(object, LocatableObject)
            and object.name in DetectableObject.__members__
        ):
            raise TypeError("object must be a DetectableObject")
        result = await vexcode_api.sees(self._device_port, object.value)
        return result

    async def angle(self, object):
        if (
            not isinstance(object, LocatableObject)
            and object.name in SeeableAngleObject.__members__
        ):
            raise TypeError("object must be an SeeableAngleObject")
        result = await vexcode_api.seesAngle(self._device_port, object.value)
        return result

    async def get_distance(self, object, unit):
        if (
            not isinstance(object, LocatableObject)
            and object.name in DetectableObject.__members__
        ):
            raise TypeError("object must be a DetectableObject")
        if not isinstance(unit, DistanceUnits):
            raise TypeError("unit must be a DistanceUnits")
        dist = await vexcode_api.seesDistance(self._device_port, object.value)
        if unit is INCHES:
            return dist / 25.4
        else:
            return dist

    async def location(self, object, axis, unit):
        if not isinstance(object, LocatableObject):
            raise TypeError("object must be a LocatableObject")
        if not isinstance(axis, PositionType):
            raise TypeError("axis must be a PositionType")
        if not isinstance(unit, DistanceUnits):
            raise TypeError("unit must be a DistanceUnits")
        location = await vexcode_api.seesLocation(
            self._device_port, object.value, axis.value
        )
        if unit is INCHES:
            return location / 25.4
        else:
            return location


class Pen(_VexCodeDevice):
    async def move(self, position):
        if not isinstance(position, PenPositionType):
            raise TypeError("position must be a PenPositionType")
        await vexcode_api.penMovePen(self._device_port, position.value)
        await wait(0.02, SECONDS)

    def set_pen_color(self, color):
        if not isinstance(color, ColorType):
            raise TypeError("color must be a ColorType")
        vexcode_api.penSetColor(self._device_port, color.value)

    def set_pen_color_rgb(self, r, g, b, a):
        if not isinstance(r, int):
            raise TypeError("red value must be an int")
        if not isinstance(g, int):
            raise TypeError("green value must be an int")
        if not isinstance(b, int):
            raise TypeError("blue value must be an int")
        if not isinstance(a, int):
            raise TypeError("opacity value must be an int")
        vexcode_api.penSetColorRGB(self._device_port, r, g, b, a)

    def set_pen_width(self, width):
        if not isinstance(width, PenWidthType):
            raise TypeError("position must be a PenWidthType")
        vexcode_api.penSetWidth(self._device_port, width.value)

    def fill(self, r, g, b, a):
        if not isinstance(r, int):
            raise TypeError("red value must be an int")
        if not isinstance(g, int):
            raise TypeError("green value must be an int")
        if not isinstance(b, int):
            raise TypeError("blue value must be an int")
        if not isinstance(a, int):
            raise TypeError("opacity value must be an int")
        vexcode_api.penFill(self._device_port, r, g, b, a)


class Bumper(_VexCodeDevice):
    def __init__(self, name, port):
        super().__init__(name, port)
        self._pressed_callbacks = []
        self._released_callbacks = []
        sensor_events.add_listener(port, self._on_sensor_event)

    def pressed(self):
        return vexcode_api.bumperPressed(self._device_port, self._device_name)

    def on_pressed(self, callback):
        self._pressed_callbacks.append(callback)

    def on_released(self, callback):
        self._released_callbacks.append(callback)

    def _on_pressed(self):
        func = get_Task_func()
        for cb in self._pressed_callbacks:
            func(call_callback(cb))

    def _on_released(self):
        func = get_Task_func()
        for cb in self._released_callbacks:
            func(call_callback(cb))

    def _on_sensor_event(self, value):
        if value is True:
            self._on_pressed()
        else:
            self._on_released()


class Distance(_VexCodeDevice):
    def found_object(self):
        return vexcode_api.distanceGetObjectFound(self._device_port, self._device_name)

    def get_distance(self, units):
        if not isinstance(units, DistanceUnits):
            raise TypeError("units must be a DistanceUnits")
        dist = vexcode_api.distanceGetDistance(self._device_port, self._device_name)
        if units is INCHES:
            return dist / 25.4
        else:
            return dist


class EyeSensor(_VexCodeDevice):
    def __init__(self, name, port):
        super().__init__(name, port)
        self._object_detected_callbacks = []
        self._object_lost_callbacks = []
        sensor_events.add_listener(port, self._on_sensor_event)

    def near_object(self):
        return vexcode_api.eyeSensorNearObject(self._device_port, self._device_name)

    def detect(self, color):
        if not isinstance(color, ColorType):
            raise TypeError("color must be a ColorType")
        sense_color = vexcode_api.eyeSensorDetect(self._device_port, self._device_name)
        return color.value == sense_color

    def brightness(self, units):
        if not isinstance(units, PercentUnits):
            raise TypeError("units must be a PercentUnits")
        return vexcode_api.eyeSensorBrightness(self._device_port, self._device_name)

    def object_detected(self, callback):
        self._object_detected_callbacks.append(callback)

    def object_lost(self, callback):
        self._object_lost_callbacks.append(callback)

    def _on_object_detected(self):
        func = get_Task_func()
        for cb in self._object_detected_callbacks:
            func(call_callback(cb))

    def _on_object_lost(self):
        func = get_Task_func()
        for cb in self._object_lost_callbacks:
            func(call_callback(cb))

    def _on_sensor_event(self, value):
        if value is True:
            self._on_object_detected()
        else:
            self._on_object_lost()


class Location(_VexCodeDevice):
    def position(self, axis, units):
        if not isinstance(axis, PositionType):
            raise TypeError("axis must be a PositionType")
        if not isinstance(units, DistanceUnits):
            raise TypeError("units must be a DistanceUnits")
        loc = vexcode_api.locationPosition(self._device_port, axis.value)
        if units is INCHES:
            return loc / 25.4
        else:
            return loc

    def position_angle(self, units):
        if not isinstance(units, RotationUnits):
            raise TypeError("units must be a RotationUnits")
        return vexcode_api.locationAngle(self._device_port)


async def wait(time, units):
    if not isinstance(time, (int, float)):
        raise TypeError("time must be a int or float")
    if not isinstance(units, TimeUnits):
        raise TypeError("units must be a TimeUnits")
    if time < 0:
        time = 0
    if units == SECONDS:
        await asyncio.sleep(time)
    else:
        await asyncio.sleep(time / 1000)


######################
# JS Promise Wrapper #
######################


class WrappedPromise:
    def __init__(self, promise):
        self.promise = promise

    def __await__(self):
        x = yield self.promise
        return x


def wrap_promise(promise):
    return WrappedPromise(promise)


###########
# Threads #
###########


def vexcode_handle_task_exception(exc):
    exc_type = type(exc).__name__
    exc_tb = exc.__traceback__
    import io

    vexcode_syntax_check_output = io.StringIO()
    import traceback

    traceback.print_exception(exc_type, exc, exc_tb, file=vexcode_syntax_check_output)
    vexcode_api.sendPythonError(vexcode_syntax_check_output.getvalue())
    vexcode_api.sendPythonRunComplete()


def vr_thread(func):
    coro = func if asyncio.iscoroutine(func) else func()
    task = asyncio.create_task(coro)

    def task_complete(fut):
        excep = fut.exception()
        if excep:
            vexcode_handle_task_exception(excep)

    task.add_done_callback(task_complete)


##########
# Utils #
#########


def stop_project():
    vexcode_api.stopProject()


def monitor_variable(*var_names):
    for var_name in var_names:
        if not isinstance(var_name, str):
            raise TypeError("variable names must be a string")
        vexcode_api.addVariableToMonitor(var_name)


def monitor_sensor(*sensor_names):
    for sensor_name in sensor_names:
        if not isinstance(sensor_name, str):
            raise TypeError("sensor names must be a string")
        vexcode_api.addSensorToMonitor(sensor_name)


__all__ = [
    ### Enums ###
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
    ### Devices ###
    "asyncio",
    "Drivetrain",
    "Motor",
    "Electromagnet",
    "Brain",
    "Rover",
    "Pen",
    "Bumper",
    "Distance",
    "EyeSensor",
    "Location",
    "wait",
    ### Events ###
    "Event",
    "brain_events",
    "sensor_events",
    ### Thread ###
    "vexcode_handle_task_exception",
    "vr_thread"
    ### Utils ###
    "stop_project",
    "monitor_variable",
    "monitor_sensor",
]
