from input.input_layer import CompassDirection, Instructions, Position, PlateauSize

class Rover:
    def __init__(self, input_name, position):
        # check name can only be string
        if not isinstance(input_name, str):
            raise TypeError('Rover name not correct type!')
        # valid names have to be between 3 and 8 characters long
        elif not 3 <= len(input_name) <= 8:
            raise ValueError('Valid Rover names have to be between 3 and 8 characters long!')
        # valid names can only be made up of alphanumerics
        elif not input_name.isalnum():
            raise ValueError('Valid Rover can only contain alphanumerics!')
        
        self.name = input_name 

        if not isinstance(position, Position):
            raise TypeError('Position is not a valid position.')
          
        self.position = position

    def check_rover_on_plateau(self, plateau):
        if 0 > self.position.x or self.position.x > plateau.max_x:
            raise ValueError(f'{self.name}\'s x co-ordinate is not on Mars!')
        elif 0 > self.position.y or self.position.y > plateau.max_y:
            raise ValueError(f'{self.name}\'s y co-ordinate is not on Mars!')
        else:
            return True

    def move_rover(self, instruction):
        if instruction == Instructions.MOVE:
            if self.position.d == CompassDirection.NORTH:
                self.position.y += 1
            elif self.position.d == CompassDirection.SOUTH:
                self.position.y -= 1
            elif self.position.d == CompassDirection.EAST:
                self.position.x += 1
            else:
                self.position.x -= 1
            
            if self.check_rover_on_plateau():
                return self.position
    
    def rotate(self, direction, instruction):
        if instruction == Instructions.RIGHT:
            if direction == CompassDirection.NORTH:
                new_direction = CompassDirection.EAST
            elif direction == CompassDirection.EAST:
                new_direction = CompassDirection.SOUTH
            elif direction == CompassDirection.SOUTH:
                new_direction = CompassDirection.WEST
            else:
                new_direction = CompassDirection.NORTH 
        elif instruction == Instructions.LEFT:
            if direction == CompassDirection.NORTH:
                new_direction = CompassDirection.WEST
            elif direction == CompassDirection.WEST:
                new_direction = CompassDirection.SOUTH
            elif direction == CompassDirection.SOUTH:
                new_direction = CompassDirection.EAST
            else:
                new_direction = CompassDirection.NORTH
        else:
            new_direction = direction
        return new_direction