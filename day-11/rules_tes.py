from main import seat_taken_next_round


# GAME RULES
def test_an_empty_seat_with_no_occupied_neighbours_gets_taken():
    assert seat_taken_next_round(False, 0, 4) == True


def test_a_taken_seat_with_no_occupied_neighbours_remains_taken():
    assert seat_taken_next_round(True, 0, 4) == True


def test_a_taken_seat_with_four_or_more_occupied_neighbours_becomes_empty():
    assert seat_taken_next_round(True, 4, 4) == False
    assert seat_taken_next_round(True, 5, 4) == False
    assert seat_taken_next_round(True, 6, 4) == False
    assert seat_taken_next_round(True, 7, 4) == False
    assert seat_taken_next_round(True, 8, 4) == False


def test_an_empty_seat_with_four_or_more_occupied_neighbours_remains_empty():
    assert seat_taken_next_round(False, 4, 4) == False
    assert seat_taken_next_round(False, 5, 4) == False
    assert seat_taken_next_round(False, 6, 4) == False
    assert seat_taken_next_round(False, 7, 4) == False
    assert seat_taken_next_round(False, 8, 4) == False


def test_a_taken_seat_with_1_to_3_occupied_neighbours_remains_taken():
    assert seat_taken_next_round(True, 1, 4) == True
    assert seat_taken_next_round(True, 2, 4) == True
    assert seat_taken_next_round(True, 3, 4) == True


def test_an_empty_seat_with_1_to_3_occupied_neighbours_remains_empty():
    assert seat_taken_next_round(False, 1, 4) == False
    assert seat_taken_next_round(False, 2, 4) == False
    assert seat_taken_next_round(False, 3, 4) == False