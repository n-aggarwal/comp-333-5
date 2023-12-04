from unit_testing_sample_code import (
    string_capitalizer,
    capitalize_list,
    integer_manipulator,
    manipulate_list,
)

# Tests


# Tests for string_capitalizer function
def test_string_capitalizer_with_word():
    assert string_capitalizer("two") == "TwO"


def test_string_capitalizer_with_single_letter():
    assert string_capitalizer("c") == "C"


def test_string_capitalizer_with_integer():
    assert string_capitalizer(4) == "FouR"


def test_string_capitalizer_with_empty_string():
    assert string_capitalizer("") == ""


# Tests for capitalize_list function
def test_capitalize_list_with_strings():
    assert capitalize_list(["two", "c", 4, ""]) == ["TwO", "C", "FouR", ""]


# Tests for integer_manipulator function
def test_integer_manipulator_with_10():
    assert integer_manipulator(10) == 66


def test_integer_manipulator_with_2():
    assert integer_manipulator(2) == 2


def test_integer_manipulator_with_3():
    assert integer_manipulator(3) == 6


def test_integer_manipulator_with_0():
    assert integer_manipulator(0) == 0


def test_integer_manipulator_with_non_integer():
    assert integer_manipulator("three") == 1


# Tests for manipulate_list function
def test_manipulate_list_with_mixed_data():
    assert manipulate_list([10, 2, 3, 0, "three"]) == [66, 2, 6, 0, 1]
