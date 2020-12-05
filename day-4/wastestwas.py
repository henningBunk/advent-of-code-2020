from main import read_passports
from main import find_field
from main import is_valid
from main import is_byr_valid
from main import is_iyr_valid
from main import is_eyr_valid
from main import is_hgt_valid
from main import is_hcl_valid
from main import is_ecl_valid
from main import is_pid_valid


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


def test_the_third_passport_is_valid_because_we_ignore_cid():
    passports = read_passports(sample_input)
    assert is_valid(passports[2]) is True


def test_the_fourth_passport_is_invalid():
    passports = read_passports(sample_input)
    assert is_valid(passports[3]) is False


### PART TWO

# byr
def test_byr_1919_is_invalid():
    assert is_byr_valid("1919") is False


def test_byr_2003_is_invalid():
    assert is_byr_valid("2003") is False


def test_byr_2002_isvalid():
    assert is_byr_valid("2002") is True


def test_byr_1920_isvalid():
    assert is_byr_valid("1920") is True

# iyr
def test_iyr_2009_is_invalid():
    assert is_iyr_valid("2009") is False


def test_iyr_2021_is_invalid():
    assert is_iyr_valid("2021") is False


def test_iyr_2010_isvalid():
    assert is_iyr_valid("2010") is True


def test_iyr_2020_isvalid():
    assert is_iyr_valid("2020") is True

# eyr
def test_eyr_2019_is_invalid():
    assert is_eyr_valid("2019") is False


def test_eyr_2031_is_invalid():
    assert is_eyr_valid("2031") is False


def test_eyr_2020_isvalid():
    assert is_eyr_valid("2020") is True


def test_eyr_2030_isvalid():
    assert is_eyr_valid("2030") is True

# hgt
def test_hgt_60in_is_valid():
    assert is_hgt_valid("60in") is True


def test_hgt_190cm_is_valid():
    assert is_hgt_valid("190cm") is True


def test_hgt_190in_is_invalid():
    assert is_hgt_valid("190in") is False


def test_hgt_190_is_invalid():
    assert is_hgt_valid("190") is False


def test_hgt_cm_is_invalid():
    assert is_hgt_valid("cm") is False


def test_hgt_190meters_is_invalid():
    assert is_hgt_valid("190meters") is False


def test_hgt_149cm_is_invalid():
    assert is_hgt_valid("149cm") is False


def test_hgt_194cm_is_invalid():
    assert is_hgt_valid("194cm") is False


def test_hgt_150cm_is_valid():
    assert is_hgt_valid("150cm") is True


def test_hgt_193cm_is_valid():
    assert is_hgt_valid("193cm") is True


def test_hgt_58in_is_invalid():
    assert is_hgt_valid("58in") is False


def test_hgt_77in_is_invalid():
    assert is_hgt_valid("77in") is False


def test_hgt_59in_is_valid():
    assert is_hgt_valid("59in") is True


def test_hgt_76in_is_valid():
    assert is_hgt_valid("76in") is True

# hcl
def test_hcl_empty_string_is_invalid():
    assert is_hcl_valid("") is False


def test_hcl_123456_is_invalid():
    assert is_hcl_valid("123456") is False


def test_hcl_hashtag_123456_is_invalid():
    assert is_hcl_valid("#123456") is True


def test_hcl_hashtag_12345g_is_invalid():
    assert is_hcl_valid("#12345g") is False


def test_hcl_hashtag_12345f_is_valid():
    assert is_hcl_valid("#12345f") is True

# ecl
def test_ecl_amb_is_valid():
    assert is_ecl_valid("amb") is True


def test_ecl_blu_is_valid():
    assert is_ecl_valid("blu") is True


def test_ecl_brn_is_valid():
    assert is_ecl_valid("brn") is True


def test_ecl_gry_is_valid():
    assert is_ecl_valid("gry") is True


def test_ecl_grn_is_valid():
    assert is_ecl_valid("grn") is True


def test_ecl_hzl_is_valid():
    assert is_ecl_valid("hzl") is True


def test_ecl_oth_is_valid():
    assert is_ecl_valid("oth") is True


def test_ecl_other_is_invalid():
    assert is_ecl_valid("other") is False


def test_ecl_123_is_invalid():
    assert is_ecl_valid("123") is False


def test_ecl_epty_string_is_invalid():
    assert is_ecl_valid("") is False

# pid
def test_pid_00000000_is_invalid():
    assert is_pid_valid("00000000") is False


def test_pid_0000000000_is_invalid():
    assert is_pid_valid("0000000000") is False


def test_pid_000000000_is_valid():
    assert is_pid_valid("000000000") is True


def test_pid_00000000A_is_invalid():
    assert is_pid_valid("00000000A") is False


def test_pid_12345_is_invalid():
    assert is_pid_valid("12345") is False


def test_pid_000012345_is_invalid():
    assert is_pid_valid("000012345") is True