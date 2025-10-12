from input.input_layer import Instructions, PlateauSize

class PlateauSizeParser:
    def parse(self, input_str):
        
        digits = [int(character) for character in input_str if character.isdigit()]
        
        if not len(digits) == 2:
            raise ValueError('Max plateau size is 9 x 9!')
        
        return tuple(digits)

class InstructionsParser:
    def parse(self, input_str):
        # turns to correct case
        upper_str = input_str.upper()
        # ignores incorrect letters
        valid_instructions = []
        for character in upper_str:
            if character in Instructions:
                valid_instructions.append(Instructions(character))
      
        return valid_instructions

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