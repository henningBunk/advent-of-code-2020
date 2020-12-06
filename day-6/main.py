
def read_in_file(file):
    return open(file).read()


def split_groups(input):
    return input.split("\n\n")


def split_members(group):
    return group.split("\n")


def count_yes_in_group(members):
    members_sets = list(map(lambda member: set(member), members))
    intersection = set.union(*members_sets)
    return len(intersection)


def count_yes_in_group_unanimous(members):
    members_sets = list(map(lambda member: set(member), members))
    intersection = set.intersection(*members_sets)
    return len(intersection)


if __name__ == '__main__':
    input = read_in_file("6.txt")
    groups = split_groups(input)

    yesses = 0
    yesses_unanimous = 0
    for group in groups:
        members = split_members(group)
        yesses += count_yes_in_group(members)
        yesses_unanimous += count_yes_in_group_unanimous(members)
    print(f"When everybodies opinion counts, there are {yesses} yesses, but if they have to agree with each other, only {yesses_unanimous}.")