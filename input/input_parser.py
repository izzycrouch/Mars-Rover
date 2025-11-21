from input.input_layer import Instructions, PlateauSize

class PlateauSizeParser:
    def parse(self, input_str):
        if ' ' in input_str:
            split_string = input_str.split(' ')
            if len(split_string) != 2:
                raise ValueError('Plateau size must be input as \'X Y\' or as \'PLATEAUXxY\'')
            try:
                X = int(split_string[0])
                Y = int(split_string[1])
                print(X,Y)
            except:
                raise ValueError('Plateau size must be numbers.')
            return (X, Y)
        
        if not ' ' in input_str:
            prefix = 'plateau'
            lower_input_str = input_str.lower()

            if lower_input_str.startswith(prefix):
                string_no_prefix = lower_input_str.replace(prefix, '')
                if 'x' not in string_no_prefix:
                    raise ValueError('Plateau size must be input as \'X Y\' or as \'PLATEAUXxY\'')
                
                split_string = string_no_prefix.split('x')
                if len(split_string) != 2:
                    raise ValueError('Plateau size must be input as \'X Y\' or as \'PLATEAUXxY\'')
                
                print(split_string)
                try:
                    X = int(split_string[0])
                    Y = int(split_string[1])
                except:
                    raise ValueError('Plateau size must be numbers.')
                return (X, Y)
        
        raise ValueError('Plateau size must be input as \'X Y\' or as \'PLATEAUXxY\'')        
        

class InstructionsParser:
    def parse(self, input_str):
        # check input string is upper
        if not input_str.isupper():
            raise ValueError('Instructions must be capitalised!')        
        
        stripped_string = input_str.replace(' ', '')

        # check only valid instructions given
        try:
            valid_instructions = []
            for character in stripped_string:
                valid_instructions.append(Instructions(character))
        except: 
            raise ValueError('Instructions not valid!')  
      
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