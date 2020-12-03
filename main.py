import re


def read_input_as_list(filename):
    return [line for line in open(filename, 'r')]

def read_input(filename):
    return open(filename, 'r').read()


def count_trees(input):
    my_position = 0
    trees = 0
    for line in input.split('\n'):
        if line[my_position] == '#':
            trees += 1
        my_position = (my_position + 3) % len(line)
    return trees


if __name__ == '__main__':
    input = read_input('3.txt')
    print(count_trees(input))
