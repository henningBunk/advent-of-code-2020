from main import count_yes_in_group
from main import count_yes_in_group_unanimous
from main import split_groups
from main import split_members

sample_input = """abc

a
b
c

ab
ac

a
a
a
a

b"""

def test_sample_input_has_5_groups():
    assert len(split_groups(sample_input)) == 5


def test_group_one_has_one_member():
    assert len(split_members(split_groups(sample_input)[0])) == 1


def test_group_two_has_three_member():
    assert len(split_members(split_groups(sample_input)[1])) == 3


def test_group_five_has_one_member():
    assert len(split_members(split_groups(sample_input)[4])) == 1


def test_group_one_has_three_unanimous_yes():
    assert count_yes_in_group_unanimous(split_members(split_groups(sample_input)[0])) == 3


def test_group_two_has_zero_unanimous_yes():
    assert count_yes_in_group_unanimous(split_members(split_groups(sample_input)[1])) == 0


def test_group_three_has_one_unanimous_yes():
    assert count_yes_in_group_unanimous(split_members(split_groups(sample_input)[2])) == 1


def test_group_four_has_one_unanimous_yes():
    assert count_yes_in_group_unanimous(split_members(split_groups(sample_input)[3])) == 1


def test_group_five_has_one_unanimous_yes():
    assert count_yes_in_group_unanimous(split_members(split_groups(sample_input)[4])) == 1


def test_group_one_has_three_yes():
    assert count_yes_in_group(split_members(split_groups(sample_input)[0])) == 3


def test_group_two_has_three_yes():
    assert count_yes_in_group(split_members(split_groups(sample_input)[1])) == 3


def test_group_three_has_three_yes():
    assert count_yes_in_group(split_members(split_groups(sample_input)[2])) == 3


def test_group_four_has_one_yes():
    assert count_yes_in_group(split_members(split_groups(sample_input)[3])) == 1