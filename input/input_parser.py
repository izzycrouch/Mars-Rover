# from input_layer import Instructions, CompassDirection, Position,PlateauSize

class PlatueSizeParser:
    def parse(self, input_str):
        
        digits = [int(character) for character in input_str if character.isdigit()]
        
        if not len(digits) == 2:
            raise ValueError('Max plateau size is 9 x 9!')
        
        return tuple(digits)

class RoverParser:
    def parse(self, input_name):
        # check name can only be string
        if not isinstance(input_name, str):
            raise TypeError('Rover name not correct type!')
        self.name = input_name

        # valid names have to be between 3 and 8 characters long
        if not 3 <= len(self.name) <= 8:
            raise ValueError('Valid Rover names have to be between 3 and 8 characters long!')
        # valid names can only be made up of alphanumerics
        if not self.name.isalnum():
            raise ValueError('Valid Rover can only contain alphanumerics!')
        
        return self.name

class  InstructionsParser:
    def parse(self, input_str):
        # turns to correct case
        upper_str = input_str.upper()
        # ignores incorrect letters
        valid_instructions = ['L', 'R', 'M']
        valid_str = ''.join([character for character in upper_str if character in valid_instructions])
        return valid_str

class PositionParser:
    def parse(self, input_str):
        # position makes N default facing direction if only co-ordinates inputted
        if len(input_str) == 2 and input_str.isdigit():    
            position = [int(input_str[0]), int(input_str[1]), 'N']
            return tuple(position)
            
        # position checks 2 values are digits if 3 characters inputted
        elif len(input_str) == 3:
            co_ordinates = input_str[0:2]
            direction = input_str[2]
            valid_directions = ['N', 'S', 'E', 'W']
            if not co_ordinates.isdigit():
                raise ValueError('Position should be X Y D! Where X = x co-ordinate, Y = y co-ordinate, and D = direction.')
            elif not direction.upper() in valid_directions:
                raise ValueError('Invalid direction, please input N or S or E or W!')
            else:
                valid_output_list = [int(co_ordinates[0]), int(co_ordinates[1]), direction.upper()]
                return tuple(valid_output_list)
        # returns error if any other length string is inputted
        else:
            raise ValueError('Position should be X Y D! Where X = x co-ordinate, Y = y co-ordinate, and D = direction.')