from input.input_parser import PlateauSizeParser, InstructionsParser, PositionParser
from input.input_layer import Instructions, CompassDirection, Position, PlateauSize
from logic.logic_layer import Rover

class TestRoverIntegration1:
    def test_plateau_parser_and_plateau_size_classes_work_together_as_intended(self):
        plateau_parser = PlateauSizeParser()
        x, y = plateau_parser.parse('5 5')
        plateau = PlateauSize(x, y)
        assert plateau.max_x == 5
        assert plateau.max_y == 5
        assert isinstance(plateau, PlateauSize)

    def test_position_parser_and_position_classes_work_toegther_as_intended(self):
        position_parser = PositionParser()
        x, y, d = position_parser.parse('1 2 N')
        d = CompassDirection(d)
        position = Position(x, y, d)
        assert position.x == 1
        assert position.y == 2
        assert position.d == CompassDirection.NORTH
        assert isinstance(position, Position)
    
    def test_instruction_parser_and_move_rover_classes_work_together_as_intended(self):
        plateau_parser = PlateauSizeParser()
        x, y = plateau_parser.parse('5 5')
        plateau = PlateauSize(x, y)
        position_parser = PositionParser()
        x, y, d = position_parser.parse('1 2 N')
        d = CompassDirection(d)
        position = Position(x, y, d)
        instructions_parser = InstructionsParser()
        instructions = instructions_parser.parse('LMLMLMLMM')
        rover = Rover(position=position)
        rover.move_rover(instructions, plateau)
        assert rover.position.x == 1
        assert rover.position.y == 3
        assert rover.position.d == CompassDirection.NORTH
        assert isinstance(position, Position)

class TestRoverIntegration2:

    def test_position_parser_and_position_classes_work_toegther_as_intended_2(self):
        position_parser = PositionParser()
        x, y, d = position_parser.parse('3 3 E')
        d = CompassDirection(d)
        position = Position(x, y, d)
        assert position.x == 3
        assert position.y == 3
        assert position.d == CompassDirection.EAST
        assert isinstance(position, Position)
    
    def test_instruction_parser_and_move_rover_classes_work_together_as_intended_2(self):
        plateau = PlateauSize(5, 5)
        position_parser = PositionParser()
        x, y, d = position_parser.parse('3 3 E')
        d = CompassDirection(d)
        position = Position(x, y, d)
        instructions_parser = InstructionsParser()
        instructions = instructions_parser.parse('MMRMMRMRRM')
        rover = Rover(position=position)
        rover.move_rover(instructions, plateau)
        assert rover.position.x == 5
        assert rover.position.y == 1
        assert rover.position.d == CompassDirection.EAST
        assert isinstance(position, Position)