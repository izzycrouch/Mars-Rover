class InputPlateau():
    def __init__(self, input):
        # check input can only be string
        if not isinstance(input, str):
            raise TypeError('Plateau input not correct type!')
        self.input = input

    def make_input_only_digits(self):
        # strips string to only digits to find size
        digits_only = []
        for character in self.input:
            if character.isdigit():
                digits_only.append(character)
                if len(digits_only) > 2:
                    raise ValueError('Plateau can be max 9 x 9!')
        return digits_only
    
    def make_input_valid(self):
        digits_only_input = self.make_input_only_digits()
        valid_output = f'{digits_only_input[0]} {digits_only_input[1]}'
        return valid_output

    # def get_max_x(self):
    #     valid_input = self.make_input_only_digits()
    #     return valid_input[0]

    # def get_max_y(self):
    #     valid_input = self.make_input_only_digits()
    #     return valid_input[1]

# class Rover():
#     def __init__(self):
#         pass

# from enum import Enum

# class Instructions(Enum):
#     LEFT = 'L'
#     RIGHT = 'R'
#     MOVE = 'M'

# class CompassDirection(Enum):
#     NORTH = 'N'
#     SOUTH = 'S'
#     EAST = 'E'
#     WEST = 'W'