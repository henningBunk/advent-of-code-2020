def read_input_as_list(filename):
    return open(filename, 'r').read()


def read_in_map(string):
    return string.splitlines()


def count_smelly_neighbours(map, y, x):
    left = x - 1 if x > 0 else x
    right = x + 1 if x < len(map[0]) - 1 else x
    top = y - 1 if y > 0 else y
    bottom = y + 1 if y < len(map) - 1 else y

    neighbours = 0 if not map[y][x] == '#' else -1
    for row in range(top, bottom + 1):
        for seat in range(left, right + 1):
            neighbours += 1 if map[row][seat] == '#' else 0
    return neighbours


def count_ugly_neighbours(map, y, x):
    neighbours = [None] * 8
    distance = 1
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    while None in neighbours:
        for i, direction in enumerate(directions):
            (down, right) = direction
            if neighbours[i] is None:
                neighbours[i] = check_seat(map, y + (down * distance), x + (right * distance))
        distance += 1
    return neighbours.count(True)


def check_seat(map, y, x):
    if not 0 <= y < len(map) or not 0 <= x < len(map[0]):
        return False
    elif map[y][x] == '#':
        return True
    elif map[y][x] == 'L':
        return False
    else:
        return None


def seat_taken_next_round(is_taken, neighbours, unacceptable_amount_of_neighbours):
    if neighbours >= unacceptable_amount_of_neighbours:
        return False
    if neighbours == 0:
        return True
    return is_taken


def predict_next_seating_situation(map, neighbour_rule_direct, unacceptable_amount_of_neighbours):
    next_map = [""] * len(map)
    for y, row in enumerate(map):
        for x, seat in enumerate(row):
            if seat == '.':
                next_map[y] += '.'
                continue
            is_taken = map[y][x] == '#'
            if neighbour_rule_direct:
                neighbours = count_smelly_neighbours(map, y, x)
            else:
                neighbours = count_ugly_neighbours(map, y, x)
            is_taken_next_round = seat_taken_next_round(is_taken, neighbours, unacceptable_amount_of_neighbours)

            next_map[y] += '#' if is_taken_next_round else 'L'
    return next_map


def run_simulation(start, neighbour_rule_direct, unacceptable_amount_of_neighbours):
    while True:
        next = predict_next_seating_situation(start, neighbour_rule_direct, unacceptable_amount_of_neighbours)
        if next == start:
            break
        start = next
    return next


def count_seats(map):
    return "".join(map).count('#')


def print_map(map):
    for row in map:
        print(row)
    print()


if __name__ == '__main__':
    # Part 1
    start = read_in_map(read_input_as_list("11.txt"))
    unacceptable_amount_of_neighbours = 4
    neighbour_rule_direct = True
    end = run_simulation(start, neighbour_rule_direct, unacceptable_amount_of_neighbours)
    print(f"There are {count_seats(end)} occupied seats when everything has settled and the travelers don't want to smell each other.\n")

    # Part 2
    start = read_in_map(read_input_as_list("11.txt"))
    unacceptable_amount_of_neighbours = 5
    neighbour_rule_direct = False
    end = run_simulation(start, neighbour_rule_direct, unacceptable_amount_of_neighbours)
    print(f"There are {count_seats(end)} occupied seats when everything has settled and the travelers don't want to see each other.")
