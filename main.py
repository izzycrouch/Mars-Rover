from input.input_parser import PlateauSizeParser, InstructionsParser, PositionParser
from input.input_layer import Instructions, CompassDirection, Position, PlateauSize
from logic.logic_layer import Rover


plateau_parser = PlateauSizeParser()
x, y = plateau_parser.parse('5 5')
plateau = PlateauSize(x, y)

print(plateau)

position_parser = PositionParser()
x, y, d = position_parser.parse('12N')
d = CompassDirection(d)
position = Position(x, y, d)
print(position)

instructions_parser = InstructionsParser()
instructions = instructions_parser.parse('LMLMLMLMM')
print(instructions)

rover = Rover('Rover1', position)
rover.move_rover(instructions, plateau)

print(rover.position)

position_parser2 = PositionParser()
x, y, d = position_parser2.parse('33E')
d = CompassDirection(d)
position2 = Position(x, y, d)
print(position2)

instructions_parser2 = InstructionsParser()
instructions2 = instructions_parser2.parse('MMRMMRMRRM')
print(instructions2)

rover2 = Rover('IzRov', position2)
rover2.move_rover(instructions2, plateau)

print(rover2.position)