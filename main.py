# Rover Start Position

        # # check start can only be string
        # if not isinstance(start_position, str):
        #     raise TypeError('Rover name not correct type!')
        # self.start_position = start_position

# Rover Start Position Tests


    # def test_default_start_co_ordinates(self):
    #     test_r = RoverParser('Rover1')
    #     assert test_r.start_position == '0 0 N'

    # def test_start_co_ordinates_correct_when_provided(self):
    #     test_r = RoverParser('Rover1', '1 2 N')
    #     assert test_r.start_position == '1 2 N'

# Rover Start Position 2

    # def get_valid_start_position(self):
        
    #     striped_position = []
    #     for character in self.start_position:
    #         if character.isalnum():
    #             striped_position.append(character)
    #     string_position = ''.join(striped_position)
        
    #     # start position makes N default facing direction if only co-ordinates inputted
    #     if len(string_position) == 2 and string_position.isdigit():    
    #         valid_start_position = f'{striped_position[0]} {striped_position[1]} N'
    #         return valid_start_position
        
    #     # start position checks 2 values are digits if 3 characters inputted
    #     elif len(string_position) == 3:
    #         pos_direction = None
    #         pos_digits_only = []
    #         for character in string_position:
                
    #             if character.isdigit():
    #                 pos_digits_only.append(character)
                
    #             elif character.isalpha():
    #                 if character.casefold() in ['n'.casefold(), 'e'.casefold(), 's'.casefold(), 'w'.casefold()]:
    #                     pos_direction = character.upper()
    #                 else:
    #                     raise ValueError('Invalid facing direction, please input N or S or E or W!')
    #             else:
    #                 raise ValueError('Invalid starting position!')
            
    #         if len(pos_digits_only) != 2:
    #             raise ValueError('Invalid start position!')

    #         valid_start_position = f'{pos_digits_only[0]} {pos_digits_only[1]} {pos_direction}'
    #         return valid_start_position
    #     else:
    #         raise ValueError('Invalid start position! Input as \'X Y D\' where X = x co-ordinate, where Y = y co-ordinate, and D = direction facing (N, S, E or W).')

    # def check_starting_postion_in_plateau(self, plateau):
    #     start_position = self.get_valid_start_position()
    #     plateau_coords = plateau.make_input_valid()

    #     if int(start_position[0]) > int(plateau_coords[0]):
    #         raise ValueError(f'{self.name}\'s starting x co-ordinate is not on Mars!')
    #     if int(start_position[2]) > int(plateau_coords[2]):
    #         raise ValueError(f'{self.name}\'s starting y co-ordinate is not on Mars!')

    #     return True

# Rover Start Position Tests 2

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
