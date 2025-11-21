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
        try:
            split_input = split_string = input_str.split(' ')
        except:
            raise ValueError('Position should be X Y D! Where X = x co-ordinate, Y = y co-ordinate, and D = direction.')
        
        if len(split_input) == 2 and split_input[0].isdigit() and split_input[1].isdigit():    
            X, y, d = [int(split_input[0]), int(split_input[1]), 'N']
            return (X, y, d)
            
        # position checks 2 values are digits if 3 values inputted
        elif len(split_input) == 3:
            
            valid_directions = ['N', 'S', 'E', 'W']
            
            if not split_input[0].isdigit() and split_input[1].isdigit():
                raise ValueError('Position should be X Y D! Where X = x co-ordinate, Y = y co-ordinate, and D = direction.')
            
            elif not split_input[2].upper() in valid_directions:
                raise ValueError('Invalid direction, please input N or S or E or W!')
            else:
                X, y, d = [int(split_input[0]), int(split_input[1]), split_input[2].upper()]
                return (X, y, d)
        
        else:
            raise ValueError('Position should be X Y D! Where X = x co-ordinate, Y = y co-ordinate, and D = direction.')