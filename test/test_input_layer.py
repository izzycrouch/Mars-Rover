import pytest

from input.input_layer import InputPlateau
from input.input_layer import InputRover

# Test InputPlateau 1
def test_plateau_class_with_valid_input():
    test_p = InputPlateau('5 5')
    assert test_p.make_input_valid() == '5 5'

# Test InputPlateau 2
def test_plateau_class_raises_error_with_incorrect_input():
    # Input type - List
    error_raised = False
    try:
        test_p = InputPlateau([55])
    except TypeError:
        error_raised = True
    assert error_raised == True
    # Input type - Dict
    error_raised = False
    try:
        test_p = InputPlateau({'x': 5, 'y': 5})
    except TypeError:
        error_raised = True
    assert error_raised == True

# Test InputPlateau 3
def test_plateau_class_removes_characters_from_string_to_make_valid():
    test_p = InputPlateau('PLATEAU5x5')
    assert test_p.make_input_only_digits() == ['5','5']
    assert test_p.make_input_valid() == '5 5'

# Test InputPlateau 4
def test_plateau_class_raises_error_if_input_too_large():
    test_p = InputPlateau('22 5')
    error_raised = False
    try:
        test_p.make_input_only_digits()
    except ValueError:
        error_raised = True
    assert error_raised == True
    error_raised = False
    try:
        test_p.make_input_valid()
    except ValueError:
        error_raised = True
    assert error_raised == True

# Test InputRover 1
def test_rover_name_is_string():
    # Test valid name
    test_r = InputRover('Rover1')
    assert test_r.name == 'Rover1'
    # Test invalid name - int
    error_raised = False
    try:
        test_r = InputRover(123)
    except TypeError:
        error_raised = True
    assert error_raised == True
    # Test invalid name - list
    error_raised = False
    try:
        test_r = InputRover(['Rover 1'])
    except TypeError:
        error_raised = True
    assert error_raised == True
    # Test invalid name - dict
    error_raised = False
    try:
        test_r = InputRover({'Name': 'Rover1'})
    except TypeError:
        error_raised = True
    assert error_raised == True

# Test InputRover 2
def test_default_start_co_ordinates():
    test_r = InputRover('Rover1')
    assert test_r.start_position == '0 0 N'

# Test InputRover 3
def test_start_co_ordinates_correct_when_provided():
    test_r = InputRover('Rover1', '1 2 N')
    assert test_r.start_position == '1 2 N'

# Test InputRover 4
def test_rover_name_is_valid():
    # Test valid name returns name if valid
    test_r = InputRover('Rover1')
    assert test_r.get_valid_name() == 'Rover1'
    # Test invalid name raises error - special characters
    test_r = InputRover('Rover1!')
    with pytest.raises(ValueError):
        test_r.get_valid_name()
        assert True
    # Test invalid name raises error - length
    test_r = InputRover('ad')
    with pytest.raises(ValueError):
        test_r.get_valid_name()
        assert True

# Test InputRover 4
def test_start_co_ordinates_raises_error_if_invalid():
    test_r = InputRover('Rover1', '3 3')
    assert test_r.get_valid_start_position() == '3 3 N'
    
    test_r = InputRover('Rover1', '33N')
    assert test_r.get_valid_start_position() == '3 3 N'

    test_r = InputRover('Rover1', '3 3 N')
    assert test_r.get_valid_start_position() == '3 3 N'

    test_r = InputRover('Rover1', 'x3, y3, E')
    with pytest.raises(ValueError):
        test_r.get_valid_start_position()
        assert True
    
    test_r = InputRover('Rover1', 'x3, y3, E')
    with pytest.raises(ValueError):
        test_r.get_valid_start_position()
        assert True
    
    test_r = InputRover('Rover1', 'abc')
    with pytest.raises(ValueError):
        test_r.get_valid_start_position()
        assert True
    
    test_r = InputRover('Rover1', '12c')
    with pytest.raises(ValueError):
        test_r.get_valid_start_position()
        assert True
    
   

