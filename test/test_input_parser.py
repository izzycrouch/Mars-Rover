import pytest

from input.input_parser import PlateauSizeParser, InstructionsParser, PositionParser
from input.input_layer import Instructions, PlateauSize

class TestPlateauParser:
    def test_plateau_class_with_valid_input(self):
        plateau = PlateauSizeParser()
        assert plateau.parse('5 5') == (5, 5)

    def test_plateau_class_works_with_larger_inputs(self):
        plateau = PlateauSizeParser()
        assert plateau.parse('10 25') == (10, 25)

    def test_plateau_class_removes_characters_from_valid_string_to_result_in_output(self):
        plateau = PlateauSizeParser()
        assert plateau.parse('PLATEAU5x5') == (5, 5)
    
    def test_plateau_class_removes_characters_from_valid_string_to_result_in_output_with_larger_sizes(self):
        plateau = PlateauSizeParser()
        assert plateau.parse('PLATEAU10x5') == (10, 5)
    
    def test_plateau_class_raises_error_if_input_string_is_one_number(self):
        plateau = PlateauSizeParser()
        with pytest.raises(ValueError, match= 'Plateau size must be input as \'X Y\' or as \'PLATEAUXxY\''):
            plateau.parse('11')
    
    def test_plateau_class_raises_error_if_input_string_has_random_characters(self):
        plateau = PlateauSizeParser()
        with pytest.raises(ValueError, match= 'Plateau size must be input as \'X Y\' or as \'PLATEAUXxY\''):
            plateau.parse('size = 10 7')
    
    def test_plateau_class_raises_error_if_input_string_is_two_letters(self):
        plateau = PlateauSizeParser()
        with pytest.raises(ValueError, match= 'Plateau size must be numbers.'):
            plateau.parse('a b')
        

class TestInstructionsParser:
    def test_instruction_parser_returns_instructions_with_valid_input(self):
        test_i = InstructionsParser()
        assert  test_i.parse('LRM') == [Instructions.LEFT, Instructions.RIGHT, Instructions.MOVE]
    
    def test_input_string_ignores_white_spaces(self):
        test_i = InstructionsParser()
        assert  test_i.parse('L R M') == [Instructions.LEFT, Instructions.RIGHT, Instructions.MOVE]
    
    def test_instruction_parser_raises_error_with_lower_case_instructions(self):
        test_i = InstructionsParser()
        with pytest.raises(ValueError, match='Instructions must be capitalised!'):
            test_i.parse('lrm')
    
    def test_instruction_parser_raises_error_with_incorrect_characters(self):
        test_i = InstructionsParser()
        with pytest.raises(ValueError, match='Instructions not valid!'):
            test_i.parse('LRMTHVDAKODMRM')
            
    
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