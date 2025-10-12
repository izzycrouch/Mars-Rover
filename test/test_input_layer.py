import pytest
from input.input_layer import Instructions, Position, PlateauSize, CompassDirection, Rover

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

class TestRover:
    def test_rover_name_is_string(self):
        # Test valid name
        test_r = Rover('Rover1')
        assert test_r.name == 'Rover1'
        # Test invalid name - int
        with pytest.raises(TypeError):
            test_r = Rover(123)
        # Test invalid name - list
        with pytest.raises(TypeError):
            test_r = Rover(['Rover 1'])
        # Test invalid name - dict
        with pytest.raises(TypeError):
            test_r = Rover({'Name': 'Rover1'})

    def test_rover_name_is_valid(self):
        # Test valid name returns name if valid
        test_r = Rover('Rover12')
        assert test_r.name == 'Rover12'
        # Test invalid name raises error - special characters
        with pytest.raises(ValueError):
            test_r = Rover('Rover1!')
        # Test invalid name raises error - length
        with pytest.raises(ValueError):
            test_r = Rover('ad')