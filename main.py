import re

def read_input(filename):
    with open(filename, 'r') as file:
        return file.read()


if __name__ == '__main__':
    input = read_input('2.txt')

    count = 0
    for line in input.split('\n'):
        match = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
        min = int(match[1])
        max = int(match[2])
        letter = match[3]
        password = match[4]

        if min <= password.count(letter) <= max:
            count += 1
    print(count)