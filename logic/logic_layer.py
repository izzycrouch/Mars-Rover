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
         
        if self.check_rover_on_plateau(plateau):
            return self.position
    
    