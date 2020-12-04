from main import read_passports
from main import find_field
from main import is_valid
from main import is_byr_valid


def test_find_field_ecl_returns_gry_for_given_data():
    input = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
    assert find_field("ecl", input) == "gry"


def test_find_field_pid_returns_860033327_for_given_data():
    input = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
    assert find_field("pid", input) == "860033327"


def test_find_field_ecl_returns_gry_for_given_multiline_data():
    input = """ecl:gry
pid:860033327"""
    assert find_field("ecl", input) == "gry"


def test_find_field_pid_returns_860033327_for_given_multiline_data():
    input = """ecl:gry
pid:860033327"""
    assert find_field("pid", input) == "860033327"


def test_find_field_deepestfear_returns_none_for_given_data():
    input = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
    assert find_field("deepestfear", input) == None


sample_input = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

def test_reading_the_password_list_should_return_four_passports():
    assert len(read_passports(sample_input)) == 4


def test_the_first_passport_has_8_fields():
    assert len(read_passports(sample_input)[0].keys()) == 8


def test_the_first_passport_has_the_field_ecl():
    assert "ecl" in read_passports(sample_input)[0].keys()


def test_the_first_passport_has_the_field_pid():
    assert "pid" in read_passports(sample_input)[0].keys()


def test_the_first_passport_has_the_field_eyr():
    assert "eyr" in read_passports(sample_input)[0].keys()


def test_the_first_passport_has_the_field_hcl():
    assert "hcl" in read_passports(sample_input)[0].keys()


def test_the_first_passport_has_the_field_byr():
    assert "byr" in read_passports(sample_input)[0].keys()


def test_the_first_passport_has_the_field_iyr():
    assert "iyr" in read_passports(sample_input)[0].keys()


def test_the_first_passport_has_the_field_cid():
    assert "cid" in read_passports(sample_input)[0].keys()


def test_the_first_passport_has_the_field_hgt():
    assert "hgt" in read_passports(sample_input)[0].keys()


def test_the_first_passport_has_ecl_set_to_gry():
    assert read_passports(sample_input)[0]["ecl"] == "gry"


def test_the_first_passport_has_pid_set_to_860033327():
    assert read_passports(sample_input)[0]["pid"] == "860033327"


def test_the_first_passport_has_eyr_set_to_2020():
    assert read_passports(sample_input)[0]["eyr"] == "2020"


def test_the_first_passport_has_hcl_set_to_hashtag_fffffd():
    assert read_passports(sample_input)[0]["hcl"] == "#fffffd"


def test_the_first_passport_has_byr_set_to_1937():
    assert read_passports(sample_input)[0]["byr"] == "1937"


def test_the_first_passport_has_iyr_set_to_2017():
    assert read_passports(sample_input)[0]["iyr"] == "2017"


def test_the_first_passport_has_cid_set_to_147():
    assert read_passports(sample_input)[0]["cid"] == "147"


def test_the_first_passport_has_hgt_set_to_183cm():
    assert read_passports(sample_input)[0]["hgt"] == "183cm"



def test_the_second_passport_has_pid_set_to_028048884():
    assert read_passports(sample_input)[1]["pid"] == "028048884"


def test_the_second_passport_has_eyr_set_to_2023():
    assert read_passports(sample_input)[1]["eyr"] == "2023"


def test_the_second_passport_has_hcl_set_to_hashtag_cfa07d():
    assert read_passports(sample_input)[1]["hcl"] == "#cfa07d"


def test_the_second_passport_has_byr_set_to_1929():
    assert read_passports(sample_input)[1]["byr"] == "1929"


def test_the_second_passport_has_iyr_set_to_2013():
    assert read_passports(sample_input)[1]["iyr"] == "2013"


def test_the_second_passport_does_not_have_the_field_ecl():
    assert "hgt" not in read_passports(sample_input)[1].keys()


def test_a_passport_without_fields_is_invalid():
    assert is_valid({}) == False


def test_a_passport_with_all_fields_is_valid():
    passport = {
        "ecl": "",
        "pid": "",
        "eyr": "",
        "hcl": "",
        "byr": "",
        "iyr": "",
        "cid": "",
        "hgt": ""
    }
    assert is_valid(passport) == True


def test_the_first_passport_is_valid():
    passports = read_passports(sample_input)
    assert is_valid(passports[0]) is True


def test_the_second_passport_is_invalid():
    passports = read_passports(sample_input)
    assert is_valid(passports[1]) is False


def test_the_third_passport_is_invalid():
    passports = read_passports(sample_input)
    assert is_valid(passports[2]) is False


def test_the_fourth_passport_is_valid():
    passports = read_passports(sample_input)
    assert is_valid(passports[3]) is True


### PART TWO

