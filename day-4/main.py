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


def is_valid_loose(passport):
    # if all(name in grades for name in students):
    required_field = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
    if all(key in passport for key in required_field):
        return True
    else:
        return False


def is_valid_harsh(passport):
    if is_valid_loose(passport) == False:
        return False
    if is_ecl_valid(passport["ecl"]) == False:
        return False
    if is_pid_valid(passport["pid"]) == False:
        return False
    if is_eyr_valid(passport["eyr"]) == False:
        return False
    if is_hcl_valid(passport["hcl"]) == False:
        return False
    if is_byr_valid(passport["byr"]) == False:
        return False
    if is_iyr_valid(passport["iyr"]) == False:
        return False
    if is_hgt_valid(passport["hgt"]) == False:
        return False
    return True


def is_byr_valid(byr):
    if len(byr) != 4:
        return False
    try:
        return 1920 <= int(byr) <= 2002
    except:
        return False


def is_iyr_valid(iyr):
    if len(iyr) != 4:
        return False
    try:
        return 2010 <= int(iyr) <= 2020
    except:
        return False


def is_hgt_valid(hgt):
    try:
        height, unit = re.match(r"(\d+)(\w+)", hgt).groups()
        if unit == "cm":
           return True if 150 <= int(height) <= 193 else False
        elif unit == "in":
            return True if 59 <= int(height) <= 76 else False
        else:
            return False
    except:
        print("FAIL!")
        return False


def is_eyr_valid(eyr):
    if len(eyr) != 4:
        return False
    try:
        return 2020 <= int(eyr) <= 2030
    except:
        return False


def is_hcl_valid(hcl):
    try:
        if re.match(r"#[a-f0-9]{6}", hcl):
            return True
        else:
            return False
    except:
        return False


def is_ecl_valid(ecl):
    valid_ecls = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return ecl in valid_ecls


def is_pid_valid(pid):
    if len(pid) != 9:
        return False
    try:
        int(pid)
        return True
    except:
        return False



if __name__ == '__main__':
    input = read_input('4.txt')
    passports = read_passports(input)
    valid = 0
    for passport in passports:
        valid += 1 if is_valid_harsh(passport) else 0
    print(valid)
