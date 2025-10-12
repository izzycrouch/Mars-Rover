import pytest

from input.input_parser import PlatueSizeParser, RoverParser, InstructionsParser
#  PositionParser

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
            assert True
        # Test invalid name raises error - length
        test_r = RoverParser()
        with pytest.raises(ValueError):
            test_r.parse('ad')
            assert True

class TestInstructionsParser:
    def test_input_string_returns_upper(self):
        test_i = InstructionsParser()
        assert  test_i.parse('lrm') == 'LRM'
    
    def test_input_string_ignores_incorrect_characters(self):
        test_i = InstructionsParser()
        assert  test_i.parse('lrmTHVDAKODMsrm') == 'LRMMRM'