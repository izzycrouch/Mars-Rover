import pytest
from logic.logic_layer import Rover, MoveResult
from input.input_layer import Instructions, CompassDirection, Position, PlateauSize

class TestRoverInit:
    def test_rover_name_returns_rover_name_with_valid_input(self):
        position = Position(0, 0, 'N')
        test_r = Rover(position=position, input_name='Rover1')
        assert test_r.name == 'Rover1'

    def test_rover_raises_error_if_input_name_is_not_valid_type(self):
        position = Position(0, 0, 'N')
        # Test invalid name - int
        with pytest.raises(TypeError, match='Rover name not correct type!'):
            test_r = Rover(position=position, input_name=123)
        # Test invalid name - list
        with pytest.raises(TypeError, match='Rover name not correct type!'):
            test_r = Rover(position=position, input_name=['123'])
    
    def test_rover_name_defaults_to_rover(self):
        # Test default name
        position = Position(0, 0, 'N')
        test_r = Rover(position=position)
        assert test_r.name == 'Rover'    

    def test_rover_raises_error_with_invalid_characters(self):
        position = Position(0, 0, 'N')
        # Test invalid name raises error - special characters
        with pytest.raises(ValueError, match='Valid Rover can only contain alphanumerics!'):
            test_r = Rover(input_name='Rover1!', position=position)
        # Test invalid name raises error - length
    
    def test_rover_raises_error_with_invalid_input_length(self):   
        position = Position(0, 0, 'N')
        with pytest.raises(ValueError, match='Valid Rover names have to be between 3 and 8 characters long!'):
            test_r = Rover(input_name='ad', position=position)
        with pytest.raises(ValueError, match='Valid Rover names have to be between 3 and 8 characters long!'):
            test_r = Rover(input_name='abcdefghi', position=position)
    
    def test_rover_position_not_instance_of_position_error_raised(self):
        with pytest.raises(TypeError, match='Position is not a valid position.'):
            test_r = Rover(position=(0, 0, 'N'))

class TestRoverOnPlateau:
    def test_rover_position_within_plateau(self):
        position = Position(0, 0, 'N')
        rover = Rover(position)
        plateau = PlateauSize(5, 5)
        assert rover.check_rover_on_plateau(plateau) == MoveResult.SUCCESS
        
        position = Position(0, 5, 'N')
        rover = Rover(position)
        plateau = PlateauSize(5, 5)
        assert rover.check_rover_on_plateau(plateau) == MoveResult.SUCCESS
    
    def test_position_returns_false_if_not_on_plateau(self):
        position = Position(0, 6, 'N')
        rover = Rover(position)
        plateau = PlateauSize(5, 5)
        assert rover.check_rover_on_plateau(plateau) == MoveResult.FELL_OFF_PLATEAU
        
        position = Position(0, -1, 'N')
        rover = Rover(position)
        plateau = PlateauSize(5, 5)
        assert rover.check_rover_on_plateau(plateau) == MoveResult.FELL_OFF_PLATEAU

class TestRoverRotate:    
    def test_rotate_method(self):
        position = Position(0, 0, CompassDirection.NORTH)
        rover = Rover(position)
        assert rover.rotate(Instructions.RIGHT) == CompassDirection.EAST
        assert rover.rotate(Instructions.LEFT)== CompassDirection.NORTH

class TestMoveRover:
    def test_move_rover_method(self):
        position = Position(0, 0, CompassDirection.NORTH)
        rover = Rover(position)
        plateau = PlateauSize(5, 5)
        rover.move_rover([Instructions.MOVE, Instructions.MOVE], plateau)
        assert rover.position.x == 0
        assert rover.position.y == 2
        assert rover.position.d == CompassDirection.NORTH

        position = Position(0, 0, CompassDirection.EAST)
        rover = Rover(position)
        plateau = PlateauSize(5, 5)
        rover.move_rover([Instructions.MOVE, Instructions.MOVE], plateau)
        assert rover.position.x == 2
        assert rover.position.y == 0
        assert rover.position.d == CompassDirection.EAST

    def test_move_rover_invokes_rotate_when_instructed(self):
        position = Position(2, 2, CompassDirection.EAST)
        rover = Rover(position)
        plateau = PlateauSize(5, 5)
        rover.move_rover([Instructions.MOVE, Instructions.MOVE, Instructions.RIGHT, Instructions.MOVE], plateau)
        assert rover.position.x == 4
        assert rover.position.y == 1
        assert rover.position.d == CompassDirection.SOUTH
    
    def test_move_returns_None_if_rover_fell_off_plateau(self):
        position = Position(3, 2, CompassDirection.EAST)
        rover = Rover(position)
        plateau = PlateauSize(5, 5)
        rover.move_rover([Instructions.MOVE, Instructions.MOVE, Instructions.MOVE], plateau)
        assert rover.position == None