from os import getcwd as cwd

from problems.problem_1.solution import is_valid_username
from problems.problem_1.solution import is_valid_username_regex
from problems.problem_2.solution import check_password
from problems.problem_3.solution import to_roman_numeral
from problems.problem_4.solution import list_perfect_numbers
from problems.problem_5.solution import read_valid_dates
from problems.problem_6.solution import saddle_points
from problems.problem_7.solution import is_magic_square
from problems.problem_8.solution import merge_sorted_arrays
from problems.problem_9.solution import decode

if __name__ == '__main__':
    # 1 | USERNAMES
    assert is_valid_username("3Carlos_") == False
    assert is_valid_username("jhapontem_2") == True

    assert is_valid_username_regex("3Carlos_") == False
    assert is_valid_username_regex("jhapontem_2") == True

    # 2 | PASSWORDS
    assert check_password("abc#1234") == True
    assert check_password("abcd1234") == False

    # 3 | ROMAN NUMBERS
    assert to_roman_numeral(4) == "IV"
    assert to_roman_numeral(58) == "LVIII"

    # 4 | PERFECT NUMBERS
    assert list_perfect_numbers(1) == []
    assert list_perfect_numbers(500) == [6, 28, 496]

    # 5 | DATES
    current_dir = cwd()
    assert read_valid_dates(current_dir + "/tests/fechas.txt") == ['2020-02-29', '2020-10-10', '2021-05-12']

    # 6 | SADDLE POINTS

    # NOTE: THIS EXAMPLE IS WRONG!
    # there are no saddle points
    # assert saddle_points([
    #     [3, 1, 3],
    #     [3, 2, 4],
    #     [2, 5, 4]
    # ]) == [(0, 2)]

    # Instead I purpose this example:
    assert saddle_points([
        [3, 1, 3],
        [3, 2, 4],
        [2, 1, 4]
    ]) == [(1, 1)]


    assert saddle_points([[5, 5], [5, 5]]) == [(0, 0), (0, 1), (1, 0), (1, 1)]

    # 7 | MAGIC SQUARE

    assert is_magic_square([
        [8, 1, 6],
        [3, 5, 7],
        [4, 9, 2]
    ]) == True

    # 8 | MERGE SORTED ARRAYS
    assert merge_sorted_arrays([1, 2, 2], [2, 3]) == [1, 2, 2, 2, 3]

    # 9 | DECODE

    # NOTE: THIS EXAMPLE IS ALSO WRONG!
    # by following the docstring description, you'll obtain as result 'secroet' instead of 'secreto'
    # assert decode([1,2,0,5,3,4,6], ['c','s','e','o','e','r','t'], 7) == ‘secreto’

    assert decode([5, 6, 7, 0, 3, 2, 1, 8, 4, 9], ['a', 'u', 'm', ' ', 'd', 'h', 'o', 'l', 'n', 'o'], 10) == 'hola mundo'
