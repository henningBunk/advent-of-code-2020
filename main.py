import re


def read_input(filename):
    return open(filename, 'r').read()


def find_field(field, data):
    match = re.search(rf"{field}:([^\s]+)", data)
    if match:
        return match.group(1)
    else:
        return None


def read_passports(input):
    passports = []
    for passport_data in input.split('\n\n'):
        passport = {
            "ecl": find_field("ecl", passport_data),
            "pid": find_field("pid", passport_data),
            "eyr": find_field("eyr", passport_data),
            "hcl": find_field("hcl", passport_data),
            "byr": find_field("byr", passport_data),
            "iyr": find_field("iyr", passport_data),
            "cid": find_field("cid", passport_data),
            "hgt": find_field("hgt", passport_data)
        }
        passport = {k: v for k, v in passport.items() if v is not None}
        passports.append(passport)
    return passports


def is_valid(passport):
    # if all(name in grades for name in students):
    required_field = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
    if all(key in passport for key in required_field):
        return True
    else:
        return False


def is_byr_valid(byr):
    return False


if __name__ == '__main__':
    input = read_input('4.txt')
    passports = read_passports(input)
    valid = 0
    for passport in passports:
        valid += 1 if is_valid(passport) else 0
    print(valid)
