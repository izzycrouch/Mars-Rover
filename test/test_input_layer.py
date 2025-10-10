import pytest
from input.input_layer import Instructions, Position, PlateauSize, CompassDirection

class TestInstructions:
    def test_instructions_raises_error(self):
        instructions = 'LRMRVM'
        with pytest.raises(ValueError):
            for instruction in instructions:
                Instructions(instruction)
    
    def test_instructions_equals_correct_command(self):
        instructions = 'LRM'
        expected_commands = [Instructions.LEFT, Instructions.RIGHT, Instructions.MOVE]
        result = [Instructions(char) for char in instructions]
        assert result == expected_commands

class TestCompassDirections:
    def test_compass_directions_raises_error(self):
        direction = 'L'
        with pytest.raises(ValueError):
            CompassDirection(direction)
    
    def test_compass_direction_equals_correct_direction(self):
        direction = 'N'
        expected_direction = CompassDirection.NORTH
        result = CompassDirection(direction)
        assert result == expected_direction

class TestPosition:
    def test_position(self):
        pos = Position(1, 2, 'N')
        assert pos.x == 1
        assert pos.y == 2
        assert pos.d == 'N'

class TestPlateauSize:
    def test_plateau_size(self):
        plateau_size = PlateauSize(6, 9)
        assert plateau_size.max_x == 6
        assert plateau_size.max_y == 9