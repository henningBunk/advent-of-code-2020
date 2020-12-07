import math

def calculate_fuel(weight):
    return math.floor(weight / 3) - 2


if __name__ == '__main__':
    input = open("1.txt").read()

    input_separated = input.split('\n')

    total_fuel = 0
    for weight in input_separated:
        fuel_need = calculate_fuel(int(weight))
        total_fuel = total_fuel + fuel_need

    print(total_fuel)