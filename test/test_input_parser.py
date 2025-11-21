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
    def test_position_parser_when_no_direction_given_direction_defaults_to_N(self):
        test_pos = PositionParser()
        assert test_pos.parse('1 2') == (1, 2, 'N')
    
    def test_position_parser_returns_tuple_with_valid_input(self):
        test_pos = PositionParser()
        result = test_pos.parse('1 2 n')
        assert isinstance(result, tuple)
        assert result == (1, 2, 'N')

    def test_position_parser_returns_tuple_with_larger_valid_input(self):
        test_pos = PositionParser()
        result = test_pos.parse('25 25 E')
        assert result == (25, 25, 'E')
    
    def test_position_parser_raises_error_if_direction_not_valid(self):
        test_pos = PositionParser()
        with pytest.raises(ValueError, match='Invalid direction, please input N or S or E or W!'):
            test_pos.parse('1 2 K')

    def test_position_parser_raises_error_for_invalid_inputs(self):
        test_pos = PositionParser()
        with pytest.raises(ValueError):
            test_pos.parse('1 E K')
        
        test_pos = PositionParser()
        with pytest.raises(ValueError):
            test_pos.parse('12N')
        
        test_pos = PositionParser()
        with pytest.raises(ValueError, match='Position should be X Y D! Where X = x co-ordinate, Y = y co-ordinate, and D = direction.'):
            test_pos.parse('1')
