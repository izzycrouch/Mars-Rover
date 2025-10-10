from input.input_layer import InputPlateau

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

