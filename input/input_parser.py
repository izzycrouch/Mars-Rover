# from input_layer import Instructions, CompassDirection, Position,PlateauSize

class  InstructionsParser:
    pass

class PlatueSizeParser:
    def parse(self, input):
        
        digits = [int(character) for character in input if character.isdigit()]
        
        if not len(digits) == 2:
            raise ValueError('Max plateau size is 9 x 9!')
        
        return tuple(digits)

class RoverParser:
    def __init__(self, name):
        # check name can only be string
        if not isinstance(name, str):
            raise TypeError('Rover name not correct type!')
        self.name = name

    def get_valid_name(self):
        # valid names have to be between 3 and 8 characters long
        if not 3 <= len(self.name) <= 8:
            raise ValueError('Valid Rover names have to be between 3 and 8 characters long!')
        
        # valid names can only be made up of alphanumerics
        if not self.name.isalnum():
            raise ValueError('Valid Rover can only contain alphanumerics!')
    
        return self.name