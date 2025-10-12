from input.input_parser import PlateauSizeParser, InstructionsParser, PositionParser
from input.input_layer import Instructions, CompassDirection, Position, PlateauSize

parser = PlateauSizeParser()
x, y = parser.parse('5 5')
plateau = PlateauSize(x, y)

print(plateau)

parser = InstructionsParser()
instructions = parser.parse('lnjnsjjmsa')

print(instructions)

parser = PositionParser()
x, y, d = parser.parse('12N')
position = Position(x, y, d)
print(position)


# Rover Start Position 2
    # def check_starting_postion_in_plateau(self, plateau):
    #     start_position = self.get_valid_start_position()
    #     plateau_coords = plateau.make_input_valid()

    #     if int(start_position[0]) > int(plateau_coords[0]):
    #         raise ValueError(f'{self.name}\'s starting x co-ordinate is not on Mars!')
    #     if int(start_position[2]) > int(plateau_coords[2]):
    #         raise ValueError(f'{self.name}\'s starting y co-ordinate is not on Mars!')

    #     return True
