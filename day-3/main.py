import re


def read_input_as_list(filename):
    return [line for line in open(filename, 'r')]


def read_input(filename):
    return open(filename, 'r').read()


def count_trees(input):
    return count_trees_w_slope(input, 3, 1)


def count_trees_w_slope(input, right, down):
    my_position = 0
    trees = 0
    for line in input.split('\n')[0::down]:
        if line[my_position] == '#':
            trees += 1
        my_position = (my_position + right) % len(line)
    return trees


if __name__ == '__main__':
    input = read_input('3.txt')
    print(f"Puzzle 1: {count_trees(input)}")

    slope_1 = count_trees_w_slope(input, 1, 1)
    slope_2 = count_trees_w_slope(input, 3, 1)
    slope_3 = count_trees_w_slope(input, 5, 1)
    slope_4 = count_trees_w_slope(input, 7, 1)
    slope_5 = count_trees_w_slope(input, 1, 2)

    print(f"Puzzle 2, Slope 1: {slope_1}")
    print(f"Puzzle 2, Slope 2: {slope_2}")
    print(f"Puzzle 2, Slope 3: {slope_3}")
    print(f"Puzzle 2, Slope 4: {slope_4}")
    print(f"Puzzle 2, Slope 5: {slope_5}")

    print(f"Multiplied it's {slope_1 * slope_2 * slope_3 * slope_4 * slope_5}")
