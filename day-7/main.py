import re


def read_input_as_list(filename):
    return [line for line in open(filename, 'r')]


def analyze_rule(rule_string):
    bags_inside = []
    for amount, color in re.findall("(\d+) (\w+ \w+)", rule_string):
        bags_inside = bags_inside + ([color] * int(amount))
    return re.match("^(\w+ \w+) bags contain", rule_string).groups()[0], bags_inside


def list_outer_bags(dict, bag):
    if bag not in dict:
        #print(f"{bag} is not in any other bag")
        return []
    #print(f"{bag} is directly contained in {dict[bag]} bags")
    list = dict[bag]
    for outer in dict[bag]:
        list = list + list_outer_bags(dict, outer)
    return list


def count_inner_bags(dict, bag):
    if bag not in dict.keys():
        return 0

    direct_childs = len(dict[bag])
    indirect_childs = 0
    for child in dict[bag]:
        indirect_childs += count_inner_bags(dict, child)
    return direct_childs + indirect_childs


if __name__ == '__main__':
    rules = read_input_as_list("7.txt")
    bag_is_contained_in = {}
    bag_contains = {}

    for rule in rules:
        bag, contents = analyze_rule(rule)

        # Puzzle 1
        for content in contents:
            if content in bag_is_contained_in:
                bag_is_contained_in[content].append(bag)
            else:
                bag_is_contained_in[content] = [bag]

        # Puzzle 2
        bag_contains[bag] = contents

    print(f"{len(set(list_outer_bags(bag_is_contained_in, 'shiny gold')))} bags can contain a shiny gold bag.")
    print(f"Your shiny gold bag must contain {count_inner_bags(bag_contains, 'shiny gold')} bags.")
