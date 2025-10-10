# from input_layer import Instructions, CompassDirection, Position,PlateauSize

class  InstructionsParser:
    pass

class PlatueSizeParser:
    def parse(self, input):
        
        digits = [int(character) for character in input if character.isdigit()]
        
        if len(digits) != 2:
            raise ValueError('Max plateau size is 9 x 9!')
        
        return tuple(digits)

class RoverParser:
    def __init__(self, name, start_position='0 0 N'):
        # check name can only be string
        if not isinstance(name, str):
            raise TypeError('Rover name not correct type!')
        self.name = name
        # check start can only be string
        if not isinstance(start_position, str):
            raise TypeError('Rover name not correct type!')
        self.start_position = start_position
    
    def get_valid_name(self):
        # valid names have to be between 3 and 8 characters long
        if not 3 <= len(self.name) <= 8:
            raise ValueError('Valid Rover names have to be between 3 and 8 characters long!')
        
        # valid names can only be made up of alphanumerics
        if not self.name.isalnum():
            raise ValueError('Valid Rover can only contain alphanumerics!')
    
        return self.name
    
    def get_valid_start_position(self):
        
        striped_position = []
        for character in self.start_position:
            if character.isalnum():
                striped_position.append(character)
        string_position = ''.join(striped_position)
        
        # start position makes N default facing direction if only co-ordinates inputted
        if len(string_position) == 2 and string_position.isdigit():    
            valid_start_position = f'{striped_position[0]} {striped_position[1]} N'
            return valid_start_position
        
        # start position checks 2 values are digits if 3 characters inputted
        elif len(string_position) == 3:
            pos_direction = None
            pos_digits_only = []
            for character in string_position:
                
                if character.isdigit():
                    pos_digits_only.append(character)
                
                elif character.isalpha():
                    if character.casefold() in ['n'.casefold(), 'e'.casefold(), 's'.casefold(), 'w'.casefold()]:
                        pos_direction = character.upper()
                    else:
                        raise ValueError('Invalid facing direction, please input N or S or E or W!')
                else:
                    raise ValueError('Invalid starting position!')
            
            if len(pos_digits_only) != 2:
                raise ValueError('Invalid start position!')

            valid_start_position = f'{pos_digits_only[0]} {pos_digits_only[1]} {pos_direction}'
            return valid_start_position
        else:
            raise ValueError('Invalid start position! Input as \'X Y D\' where X = x co-ordinate, where Y = y co-ordinate, and D = direction facing (N, S, E or W).')

    def check_starting_postion_in_plateau(self, plateau):
        start_position = self.get_valid_start_position()
        plateau_coords = plateau.make_input_valid()

        if int(start_position[0]) > int(plateau_coords[0]):
            raise ValueError(f'{self.name}\'s starting x co-ordinate is not on Mars!')
        if int(start_position[2]) > int(plateau_coords[2]):
            raise ValueError(f'{self.name}\'s starting y co-ordinate is not on Mars!')

        return True