from main import predict_next_seating_situation
from main import read_in_map
from main import count_seats
from main import run_simulation


def test_predict_next_seating_situation_predicts_t1_from_t0():
    assert predict_next_seating_situation(t0, True, 4) == t1


def test_predict_next_seating_situation_predicts_t2_from_t1():
    assert predict_next_seating_situation(t1, True, 4) == t2


def test_predict_next_seating_situation_predicts_t3_from_t2():
    assert predict_next_seating_situation(t2, True, 4) == t3


def test_predict_next_seating_situation_predicts_t4_from_t3():
    assert predict_next_seating_situation(t3, True, 4) == t4


def test_predict_next_seating_situation_predicts_t4_from_t4():
    assert predict_next_seating_situation(t4, True, 4) == t4


def test_t4_has_37_occupied_seats():
    assert count_seats(t4) == 37


def test_run_simulation_for_t0_gives_t4():
    assert run_simulation(t0, True, 4) == t4


t0 = read_in_map("""
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
""".strip())

t1 = read_in_map("""
#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
""".strip())

t2 = read_in_map("""
#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
""".strip())

t3 = read_in_map("""
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##
""".strip())

t4 = read_in_map("""
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
""".strip())
