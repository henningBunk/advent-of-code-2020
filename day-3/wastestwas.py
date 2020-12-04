from main import count_trees
from main import count_trees_w_slope

sample_input = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


def test_count_trees_puzzle_1():
    assert count_trees(sample_input) == 7


def test_count_trees_slope_1_1():
    assert count_trees_w_slope(sample_input, 1, 1) == 2


def test_count_trees_slope_3_1():
    assert count_trees_w_slope(sample_input, 3, 1) == 7


def test_count_trees_slope_5_1():
    assert count_trees_w_slope(sample_input, 5, 1) == 3


def test_count_trees_slope_7_1():
    assert count_trees_w_slope(sample_input, 7, 1) == 4


def test_count_trees_slope_1_2():
    assert count_trees_w_slope(sample_input, 1, 2) == 2