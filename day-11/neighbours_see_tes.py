from main import count_ugly_neighbours
from main import read_in_map


def test_a_full_1_1_map_has_no_neighbours():
    map = [['#']]
    assert count_ugly_neighbours(map, 0, 0) == 0


def test_an_empty_1_1_map_has_no_neighbours():
    map = [['L']]
    assert count_ugly_neighbours(map, 0, 0) == 0


def test_a_full_1_2_map_has_1_neighbour():
    map = [['#'], ['#']]
    assert count_ugly_neighbours(map, 0, 0) == 1
    assert count_ugly_neighbours(map, 1, 0) == 1


def test_an_empty_1_2_map_has_0_neighbour():
    map = [['L'], ['L']]
    assert count_ugly_neighbours(map, 0, 0) == 0
    assert count_ugly_neighbours(map, 1, 0) == 0


def test_a_full_2_1_map_has_1_neighbour():
    map = [['#', '#']]
    assert count_ugly_neighbours(map, 0, 0) == 1
    assert count_ugly_neighbours(map, 0, 1) == 1


def test_an_empty_2_1_map_has_0_neighbour():
    map = [['L', 'L']]
    assert count_ugly_neighbours(map, 0, 0) == 0
    assert count_ugly_neighbours(map, 0, 1) == 0


def test_some_seats_from_t0():
    map = read_in_map(t0)
    assert count_ugly_neighbours(map, 0, 0) == 3
    assert count_ugly_neighbours(map, 0, 1) == 5
    assert count_ugly_neighbours(map, 0, 2) == 5
    assert count_ugly_neighbours(map, 0, 3) == 5
    assert count_ugly_neighbours(map, 0, 4) == 5
    assert count_ugly_neighbours(map, 0, 5) == 5
    assert count_ugly_neighbours(map, 0, 6) == 5
    assert count_ugly_neighbours(map, 0, 7) == 5
    assert count_ugly_neighbours(map, 0, 8) == 5
    assert count_ugly_neighbours(map, 0, 9) == 3

    assert count_ugly_neighbours(map, 7, 0) == 5
    assert count_ugly_neighbours(map, 7, 1) == 6
    assert count_ugly_neighbours(map, 7, 2) == 8
    assert count_ugly_neighbours(map, 7, 3) == 8
    assert count_ugly_neighbours(map, 7, 4) == 8
    assert count_ugly_neighbours(map, 7, 5) == 8
    assert count_ugly_neighbours(map, 7, 6) == 8
    assert count_ugly_neighbours(map, 7, 7) == 8
    assert count_ugly_neighbours(map, 7, 8) == 7
    assert count_ugly_neighbours(map, 7, 9) == 4


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

def test_some_seats_from_u0():
    map = read_in_map(u0)
    assert count_ugly_neighbours(map, 0, 0) == 2
    assert count_ugly_neighbours(map, 0, 1) == 2
    assert count_ugly_neighbours(map, 0, 2) == 3
    assert count_ugly_neighbours(map, 0, 3) == 3
    assert count_ugly_neighbours(map, 0, 4) == 4
    assert count_ugly_neighbours(map, 0, 5) == 1
    assert count_ugly_neighbours(map, 0, 6) == 2
    assert count_ugly_neighbours(map, 0, 7) == 0
    assert count_ugly_neighbours(map, 0, 8) == 2

    assert count_ugly_neighbours(map, 4, 3) == 8

u0 = """
.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....
""".strip()

def test_empty_seats_block_visibility():
    map = read_in_map(v0)
    assert count_ugly_neighbours(map, 1, 1) == 0

v0 = """
.............
.L.L.#.#.#.#.
.............
""".strip()