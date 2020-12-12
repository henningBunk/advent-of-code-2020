import re


def read_input_as_list(filename):
    return [re.match(r"(\w)(\d+)", line.strip()).groups() for line in open(filename, 'r')]


def move_ship_directly(input):
    north = 0
    east = 0
    facing = 90
    for direction, amount in input:
        amount = int(amount)
        if direction == 'E':
            east += amount
        elif direction == 'W':
            east -= amount
        elif direction == 'N':
            north += amount
        elif direction == 'S':
            north -= amount
        elif direction == 'R':
            facing = facing + amount
        elif direction == 'L':
            facing = facing - amount
        elif direction == 'F':
            if facing % 360 == 0:
                north += amount
            elif facing % 360 == 90:
                east += amount
            elif facing % 360 == 180:
                north -= amount
            elif facing % 360 == 270:
                east -= amount
    print_ship_position(east, north)


# TODO this should be done way smarter via matrix multiplication for scaling and rotation
def move_ship_via_waypoint():
    waypoint = [10, 1]
    north = 0
    east = 0
    for direction, amount in input:
        amount = int(amount)
        new_waypoint = [waypoint[0], waypoint[1]]
        # MOVE THE WAYPOINT
        if direction == 'E':
            new_waypoint[0] += amount
        elif direction == 'W':
            new_waypoint[0] += -amount
        elif direction == 'N':
            new_waypoint[1] += amount
        elif direction == 'S':
            new_waypoint[1] += -amount

        # ROTATE THE WAYPOINT
        elif direction == 'R':
            if amount == 90:
                new_waypoint[0] = waypoint[1]
                new_waypoint[1] = -waypoint[0]
            if amount == 180:
                new_waypoint[0] = -waypoint[0]
                new_waypoint[1] = -waypoint[1]
            if amount == 270:
                new_waypoint[0] = -waypoint[1]
                new_waypoint[1] = waypoint[0]
        elif direction == 'L':
            if amount == 90:
                new_waypoint[0] = -waypoint[1]
                new_waypoint[1] = waypoint[0]
            if amount == 180:
                new_waypoint[0] = -waypoint[0]
                new_waypoint[1] = -waypoint[1]
            if amount == 270:
                new_waypoint[0] = waypoint[1]
                new_waypoint[1] = -waypoint[0]

        # MOVE THE SHIP TO THE WAYPOINT
        elif direction == 'F':
            east += waypoint[0] * amount
            north += waypoint[1] * amount
        waypoint = new_waypoint
    print_ship_position(east, north)


def print_ship_position(east, north):
    print(f"The ship is {f'{east} degrees east.' if east >= 0 else f'{-east} degrees west.'}")
    print(f"The ship is {f'{north} degrees north.' if north >= 0 else f'{-north} degrees south.'}")
    print(f"The Manhatten distance is {abs(north) + abs(east)} blocks")


if __name__ == '__main__':
    input = read_input_as_list("11.txt")
    # PART 1
    move_ship_directly(input)
    # PART 2
    move_ship_via_waypoint()
