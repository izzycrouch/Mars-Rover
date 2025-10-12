from enum import Enum

class Instructions(Enum):
    LEFT = 'L'
    RIGHT = 'R'
    MOVE = 'M'

class CompassDirection(Enum):
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'

class Position:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
    
    def __str__(self):
        return f'{self.x} {self.y} {self.d}'

class PlateauSize:
    def __init__(self, x, y):
        self.max_x = x
        self.max_y = y
    
    def __str__(self):
        return f'{self.max_x} {self.max_y}'