import pytest
from main import find_row


def test_find_row_for_one_row_is_that_row():
    assert find_row("", [10]) == 10


def test_find_row_must_have_enough_information_in_the_input():
    with pytest.raises(Exception):
        find_row("", list(range(0, 17)))


def test_find_row_only_takes_F_and_B_as_code_input():
    with pytest.raises(Exception):
        find_row("ACDEGHIJKLMNOPQRSTUVWXYZ", list(range(0, 128)))


def test_find_row_for_two_rows_returns_0_when_the_code_is_f():
    assert find_row("F", list(range(0, 2))) == 0


def test_find_row_for_two_rows_returns_1_when_the_code_is_b():
    assert find_row("B", list(range(0, 2))) == 1


def test_find_row_for_four_rows_returns_0_when_the_code_is_ff():
    assert find_row("FF", list(range(0, 4))) == 0


def test_find_row_for_four_rows_returns_1_when_the_code_is_fb():
    assert find_row("FB", list(range(0, 4))) == 1


def test_find_row_for_four_rows_returns_2_when_the_code_is_bf():
    assert find_row("BF", list(range(0, 4))) == 2


def test_find_row_for_four_rows_returns_3_when_the_code_is_bb():
    assert find_row("BB", list(range(0, 4))) == 3


def test_find_row_for_eight_rows_returns__when_the_code_is_fff():
    assert find_row("FFF", list(range(0, 8))) == 0


def test_find_row_for_eight_rows_returns__when_the_code_is_ffb():
    assert find_row("FFB", list(range(0, 8))) == 1


def test_find_row_for_eight_rows_returns__when_the_code_is_fbf():
    assert find_row("FBF", list(range(0, 8))) == 2


def test_find_row_for_eight_rows_returns__when_the_code_is_fbb():
    assert find_row("FBB", list(range(0, 8))) == 3


def test_find_row_for_eight_rows_returns__when_the_code_is_bff():
    assert find_row("BFF", list(range(0, 8))) == 4


def test_find_row_for_eight_rows_returns__when_the_code_is_bfb():
    assert find_row("BFB", list(range(0, 8))) == 5


def test_find_row_for_eight_rows_returns__when_the_code_is_bbf():
    assert find_row("BBF", list(range(0, 8))) == 6


def test_find_row_for_eight_rows_returns__when_the_code_is_bbb():
    assert find_row("BBB", list(range(0, 8))) == 7
