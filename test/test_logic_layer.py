import pytest
from logic.logic_layer import Rover
from input.input_layer import Instructions, CompassDirection, Position, PlateauSize

class TestRover:
    def test_rover_name_is_string(self):
        # Test valid name
        position = Position(0, 0, 'N')
        test_r = Rover('Rover1', position)
        assert test_r.name == 'Rover1'
        # Test invalid name - int
        with pytest.raises(TypeError):
            test_r = Rover(123, position)
        # Test insvalid name - list
        with pytest.raises(TypeError):
            test_r = Rover(['Rover 1', position])
        # Test invalid name - dict
        with pytest.raises(TypeError):
            test_r = Rover({'Name': 'Rover1'}, position)

    def test_rover_name_is_valid(self):
        # Test valid name returns name if valid
        position = Position(0, 0, 'N')
        test_r = Rover('Rover12', position)
        assert test_r.name == 'Rover12'
        # Test invalid name raises error - special characters
        with pytest.raises(ValueError):
            test_r = Rover('Rover1!', position)
        # Test invalid name raises error - length
        with pytest.raises(ValueError):
            test_r = Rover('ad', position)
    
    def test_rover_position_not_instance_of_position_error_raised(self):
        with pytest.raises(TypeError):
            test_r = Rover('Rover12', (0, 0, 'N'))
    
    def test_position_within_plateau(self):
        position = Position(0, 0, 'N')
        rover = Rover('Rover12', position)
        plateau = PlateauSize(5, 5)
        assert rover.check_rover_on_plateau(plateau) == True
        
        position = Position(0, 5, 'N')
        rover = Rover('Rover12', position)
        plateau = PlateauSize(5, 5)
        assert rover.check_rover_on_plateau(plateau) == True
    
    def test_position_raises_error_if_not_within_plateau(self):
        position = Position(0, 6, 'N')
        rover = Rover('Rover12', position)
        plateau = PlateauSize(5, 5)
        with pytest.raises(ValueError):
            rover.check_rover_on_plateau(plateau)
        
        position = Position(0, -1, 'N')
        rover = Rover('Rover12', position)
        plateau = PlateauSize(5, 5)
        with pytest.raises(ValueError):
            rover.check_rover_on_plateau(plateau)
    
    def test_rotate_method(self):
        position = Position(0, 0, 'N')
        rover = Rover('Rover1', position)
        assert rover.rotate(CompassDirection.NORTH, Instructions.RIGHT) == CompassDirection.EAST
        assert rover.rotate(CompassDirection.SOUTH, Instructions.MOVE) == CompassDirection.SOUTH
        assert rover.rotate(CompassDirection.SOUTH, Instructions.LEFT) == CompassDirection.EAST