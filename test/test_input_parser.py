import pytest

from input.input_parser import PlatueSizeParser, RoverParser, InstructionsParser, PositionParser
from input.input_layer import Instructions

class TestPlateauParser:
    def test_plateau_class_with_valid_input(self):
        plateau = PlatueSizeParser()
        assert plateau.parse('5 5') == (5, 5)

    def test_plateau_class_raises_error_with_incorrect_input(self):
        plateau = PlatueSizeParser()
        with pytest.raises(ValueError):
            plateau.parse('10 7')

    def test_plateau_class_removes_characters_from_string_to_make_valid(self):
        plateau = PlatueSizeParser()
        assert plateau.parse('PLATEAU5x5') == (5, 5)
        
class TestRoverParser:
    def test_rover_name_is_string(self):
        # Test valid name
        test_r = RoverParser()
        assert test_r.parse('Rover1') == 'Rover1'
        # Test invalid name - int
        test_r = RoverParser()
        with pytest.raises(TypeError):
            test_r.parse(123)
        # Test invalid name - list
        test_r = RoverParser()
        with pytest.raises(TypeError):
            test_r.parse(['Rover 1'])
        # Test invalid name - dict
        test_r = RoverParser()
        with pytest.raises(TypeError):
            test_r.parse({'Name': 'Rover1'})

    def test_rover_name_is_valid(self):
        # Test valid name returns name if valid
        test_r = RoverParser()
        assert test_r.parse('Rover12') == 'Rover12'
        # Test invalid name raises error - special characters
        test_r = RoverParser()
        with pytest.raises(ValueError):
            test_r.parse('Rover1!')
        # Test invalid name raises error - length
        test_r = RoverParser()
        with pytest.raises(ValueError):
            test_r.parse('ad')

class TestInstructionsParser:
    def test_input_string_returns_upper(self):
        test_i = InstructionsParser()
        assert  test_i.parse('lrm') == [Instructions.LEFT, Instructions.RIGHT, Instructions.MOVE]
    
    def test_input_string_ignores_incorrect_characters(self):
        test_i = InstructionsParser()
        assert  test_i.parse('lrmTHVDAKODMsrm') == [Instructions.LEFT, Instructions.RIGHT, Instructions.MOVE, Instructions.MOVE, Instructions.RIGHT, Instructions.MOVE]

class TestPositionParser:
    def test_when_no_direction_given_direction_defaults_to_N(self):
        test_pos = PositionParser()
        assert test_pos.parse('12') == (1, 2, 'N')
    
    def test_valid_input_string_returns_tuple(self):
        test_pos = PositionParser()
        assert test_pos.parse('12n') == (1, 2, 'N')
    
    def test_invalid_input_string_raises_error(self):
        test_pos = PositionParser()
        with pytest.raises(ValueError):
            test_pos.parse('12K')

        test_pos = PositionParser()
        with pytest.raises(ValueError):
            test_pos.parse('1EK')
        
        test_pos = PositionParser()
        with pytest.raises(ValueError):
            test_pos.parse('1')
        
        test_pos = PositionParser()
        with pytest.raises(ValueError):
            test_pos.parse('123W')