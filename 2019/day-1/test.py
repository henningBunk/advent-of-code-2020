from main import calculate_fuel


def test_weight_12_should_be_2_fuel():
    assert calculate_fuel(12) == 2


def test_weight_14_should_be_2_fuel():
    assert calculate_fuel(14) == 2


def test_weight_1969_should_be_654_fuel():
    assert calculate_fuel(1969) == 654


def test_weight_100756_should_be_33583_fuel():
    assert calculate_fuel(100756) == 33583