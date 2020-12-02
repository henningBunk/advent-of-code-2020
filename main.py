import re


def read_input(filename):
    return [line for line in open(filename, 'r')]


if __name__ == '__main__':
    input = read_input('2.txt')

    count = 0
    for line in input:
        match = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
        min = int(match[1])
        max = int(match[2])
        letter = match[3]
        password = match[4]

        if (password[min - 1] == letter) ^ (password[max - 1] == letter):
            count += 1

    print(count)