from input.input_layer import CompassDirection, Instructions, Position, PlateauSize
from enum import Enum

class MoveResult(Enum):
    SUCCESS = 'Success'
    CRASHED = 'Crashed'
    FELL_OFF_PLATEAU = 'Fell'

default_position = Position(0, 0, 'N')

class Rover:
    def __init__(self, position: Position =default_position , input_name: str = 'Rover'):

        if input_name:
            self.name = input_name 
        else:
            self.name = 'Rover' 

        if not isinstance(position, Position):
            raise TypeError('Position is not a valid position.')
        
        if position:
            self.position = position  
        else:
            self.position = default_position


    def check_rover_on_plateau(self, plateau):
        x_on_mars = False
        y_on_mars = False

        if 0 <= self.position.x <= plateau.max_x:
            x_on_mars = True
        if 0 <= self.position.y <= plateau.max_y:
            y_on_mars = True
        
        if x_on_mars and y_on_mars:
            return MoveResult.SUCCESS
        
        return MoveResult.FELL_OFF_PLATEAU  

    def rotate(self, instruction):
        if instruction == Instructions.RIGHT:
            if self.position.d == CompassDirection.NORTH:
                new_direction = CompassDirection.EAST
            elif self.position.d == CompassDirection.EAST:
                new_direction = CompassDirection.SOUTH
            elif self.position.d == CompassDirection.SOUTH:
                new_direction = CompassDirection.WEST
            else:
                new_direction = CompassDirection.NORTH 
        elif instruction == Instructions.LEFT:
            if self.position.d == CompassDirection.NORTH:
                new_direction= CompassDirection.WEST
            elif self.position.d == CompassDirection.WEST:
                new_direction= CompassDirection.SOUTH
            elif self.position.d == CompassDirection.SOUTH:
                new_direction = CompassDirection.EAST
            else:
                new_direction = CompassDirection.NORTH
        else:
            new_direction = self.position.d
        
        self.position.d = new_direction
        return self.position.d
    
    def move_rover(self, instructions, plateau):
        for instruction in instructions: 
            if instruction == Instructions.MOVE:
                if self.position.d == CompassDirection.NORTH:
                    self.position.y += 1
                elif self.position.d == CompassDirection.SOUTH:
                    self.position.y -= 1
                elif self.position.d == CompassDirection.EAST:
                    self.position.x += 1
                else:
                    self.position.x -= 1
            else:
                self.rotate(instruction)
         
        if self.check_rover_on_plateau(plateau) == MoveResult.SUCCESS:
            return self.position
        elif self.check_rover_on_plateau(plateau) == MoveResult.FELL_OFF_PLATEAU:
            self.position = None
            return self.position
    
    