from input.input_parser import PlateauSizeParser, InstructionsParser, PositionParser, RoverNameParser
from input.input_layer import Instructions, CompassDirection, Position, PlateauSize
from logic.logic_layer import Rover


# plateau_parser = PlateauSizeParser()
# x, y = plateau_parser.parse('5 5')
# plateau = PlateauSize(x, y)

# print(plateau)

# position_parser = PositionParser()
# x, y, d = position_parser.parse('1 2 N')
# d = CompassDirection(d)
# position = Position(x, y, d)
# print(position)

# instructions_parser = InstructionsParser()
# instructions = instructions_parser.parse('LMLMLMLMM')
# print(instructions)

# rover = Rover(position=position)
# rover.move_rover(instructions, plateau)

# print(rover.position)

# position_parser2 = PositionParser()
# x, y, d = position_parser2.parse('3 3 E')
# d = CompassDirection(d)
# position2 = Position(x, y, d)
# print(position2)

# instructions_parser2 = InstructionsParser()
# instructions2 = instructions_parser2.parse('MMRMMRMRRM')
# print(instructions2)

# rover2 = Rover(position=position2)
# rover2.move_rover(instructions2, plateau)

# print(rover2.position)

import subprocess

def start_up_message():
    return subprocess.run(["./start-up-script.sh", 
                "arguments"], shell=True)


def generate_plateau():    
    while True:
    
        print('\nWhat sized Plateau would you like?')
        print('Note: input as \'X Y\' or \'PLATEAUXxY\'.\n')
        
        plateua_size = input()
        plateau_parser = PlateauSizeParser()
        
        try:
            x, y = plateau_parser.parse(plateua_size)
            plateau = PlateauSize(x, y)
            print(f'\nFab! Your Plateau is {x} by {y}.')
        
        except ValueError as e:
            print(f'\nERROR: {e}')
            print('Try again!')
        else:
            break
    
    return plateau


def generate_rover():
    while True:
        print('\nWhat would you like to call your Rover?')
        print('Note: Must be between 3 and 8 characters long and only consist of alphanumericals.\n')
        
        rover_name = input()
        rover_name_parser = RoverNameParser()
        try:
            name = rover_name_parser.parse(rover_name)
        except ValueError as e:
            print(f'\nERROR: {e}')
            print('Try again!')
        else:
            break
    
    while True:
        
        print('\nWhat position would you your Rover to start at?')
        print('Note: input as X Y D. (X = x co-ordinate, Y = y co-ordinate, and D = direction)\n')
        
        start_position = input()
        position_parser = PositionParser()

        try:
            x, y, d = position_parser.parse(start_position)
            position = Position(x, y, d)
        except ValueError as e:
            print(f'\nERROR: {e}')
            print('Try again!')
        else:
            break
    
    rover = Rover(input_name=name, position=position)
    return rover



def activate_mars_rover():
    # start_up_message()
    plateau = generate_plateau()
    rover = generate_rover()

activate_mars_rover()