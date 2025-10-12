import pytest

from input.input_parser import PlatueSizeParser, RoverParser

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
        test_r = RoverParser('Rover1')
        assert test_r.name == 'Rover1'
        # Test invalid name - int
        error_raised = False
        try:
            test_r = RoverParser(123)
        except TypeError:
            error_raised = True
        assert error_raised == True
        # Test invalid name - list
        error_raised = False
        try:
            test_r = RoverParser(['Rover 1'])
        except TypeError:
            error_raised = True
        assert error_raised == True
        # Test invalid name - dict
        error_raised = False
        try:
            test_r = RoverParser({'Name': 'Rover1'})
        except TypeError:
            error_raised = True
        assert error_raised == True

    def test_rover_name_is_valid(self):
        # Test valid name returns name if valid
        test_r = RoverParser('Rover1')
        assert test_r.get_valid_name() == 'Rover1'
        # Test invalid name raises error - special characters
        test_r = RoverParser('Rover1!')
        with pytest.raises(ValueError):
            test_r.get_valid_name()
            assert True
        # Test invalid name raises error - length
        test_r = RoverParser('ad')
        with pytest.raises(ValueError):
            test_r.get_valid_name()
            assert True

#     def test_start_co_ordinates_raises_error_if_invalid(self):
#         test_r = RoverParser('Rover1', '3 3')
#         assert test_r.get_valid_start_position() == '3 3 N'
        
#         test_r = RoverParser('Rover1', '33N')
#         assert test_r.get_valid_start_position() == '3 3 N'

#         test_r = RoverParser('Rover1', '3 3 N')
#         assert test_r.get_valid_start_position() == '3 3 N'

#         test_r = RoverParser('Rover1', 'x3, y3, E')
#         with pytest.raises(ValueError):
#             test_r.get_valid_start_position()
#             assert True
        
#         test_r = RoverParser('Rover1', 'x3, y3, E')
#         with pytest.raises(ValueError):
#             test_r.get_valid_start_position()
#             assert True
        
#         test_r = RoverParser('Rover1', 'abc')
#         with pytest.raises(ValueError):
#             test_r.get_valid_start_position()
#             assert True
        
#         test_r = RoverParser('Rover1', '12c')
#         with pytest.raises(ValueError):
#             test_r.get_valid_start_position()
#             assert True
        
#     def test_start_co_ordinates_in_plateau(self):
#         test_r = RoverParser('Rover1', '1 2 N')
#         test_p = PlatueSizeParser('5 5')
#         assert test_r.check_starting_postion_in_plateau(test_p) == True

#         test_r = RoverParser('Rover1', '5 6 N')
#         test_p = PlatueSizeParser('5 5')
#         with pytest.raises(ValueError):
#             test_r.check_starting_postion_in_plateau(test_p)
#             assert True
        
#         test_r = RoverParser('Rover1', '12 6 N')
#         test_p = PlatueSizeParser('5 5')
#         with pytest.raises(ValueError):
#             test_r.check_starting_postion_in_plateau(test_p)
#             assert True
