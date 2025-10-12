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
            
class Rover:
    def __init__(self, input_name):
        # check name can only be string
        if not isinstance(input_name, str):
            raise TypeError('Rover name not correct type!')
        # valid names have to be between 3 and 8 characters long
        elif not 3 <= len(input_name) <= 8:
            raise ValueError('Valid Rover names have to be between 3 and 8 characters long!')
        # valid names can only be made up of alphanumerics
        elif not input_name.isalnum():
            raise ValueError('Valid Rover can only contain alphanumerics!')
        else:
            self.name = input_name  