from main import count_smelly_neighbours
from main import read_in_map


def test_a_full_1_1_map_has_no_neighbours():
    map = [['#']]
    assert count_smelly_neighbours(map, 0, 0) == 0


def test_an_empty_1_1_map_has_no_neighbours():
    map = [['L']]
    assert count_smelly_neighbours(map, 0, 0) == 0


def test_a_full_1_2_map_has_1_neighbour():
    map = [['#'], ['#']]
    assert count_smelly_neighbours(map, 0, 0) == 1
    assert count_smelly_neighbours(map, 1, 0) == 1


def test_an_empty_1_2_map_has_0_neighbour():
    map = [['L'], ['L']]
    assert count_smelly_neighbours(map, 0, 0) == 0
    assert count_smelly_neighbours(map, 1, 0) == 0


def test_a_full_2_1_map_has_1_neighbour():
    map = [['#', '#']]
    assert count_smelly_neighbours(map, 0, 0) == 1
    assert count_smelly_neighbours(map, 0, 1) == 1


def test_an_empty_2_1_map_has_0_neighbour():
    map = [['L', 'L']]
    assert count_smelly_neighbours(map, 0, 0) == 0
    assert count_smelly_neighbours(map, 0, 1) == 0


def test_some_seats_from_t0():
    map = read_in_map(t0)
    assert count_smelly_neighbours(map, 0, 0) == 2
    assert count_smelly_neighbours(map, 0, 1) == 5
    assert count_smelly_neighbours(map, 0, 2) == 4
    assert count_smelly_neighbours(map, 0, 3) == 4
    assert count_smelly_neighbours(map, 0, 4) == 5
    assert count_smelly_neighbours(map, 0, 5) == 4
    assert count_smelly_neighbours(map, 0, 6) == 3
    assert count_smelly_neighbours(map, 0, 7) == 4
    assert count_smelly_neighbours(map, 0, 8) == 3
    assert count_smelly_neighbours(map, 0, 9) == 3

    assert count_smelly_neighbours(map, 7, 0) == 2
    assert count_smelly_neighbours(map, 7, 1) == 5
    assert count_smelly_neighbours(map, 7, 2) == 5
    assert count_smelly_neighbours(map, 7, 3) == 7
    assert count_smelly_neighbours(map, 7, 4) == 6
    assert count_smelly_neighbours(map, 7, 5) == 6
    assert count_smelly_neighbours(map, 7, 6) == 5
    assert count_smelly_neighbours(map, 7, 7) == 4
    assert count_smelly_neighbours(map, 7, 8) == 4
    assert count_smelly_neighbours(map, 7, 9) == 2

t0 = """
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
""".strip()