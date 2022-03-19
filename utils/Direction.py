import enum


class Direction(str, enum.Enum):
    EAST: str = "EAST"
    WEST: str = "WEST"
    SOUTH: str = "SOUTH"
    NORTH: str = "NORTH"

    # To be able to compare Strings
    def __str__(self):
        return str(self.value)
