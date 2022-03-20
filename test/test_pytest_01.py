import pytest

import main


@pytest.fixture(autouse=True, scope='session')
def directions():
    pytest.directions = ["NORTH", "SOUTH", "EAST", "WEST"]
    pytest.direction_1 = ["NORTH", "SOUTH", "EAST", "WEST"]
    pytest.direction_2 = ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]
    pytest.direction_3 = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    pytest.direction_4 = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"]
    pytest.direction_5 = ["NORTH", "WEST", "SOUTH", "EAST"]


def test_empty_path():
    assert main.init([]) == []


@pytest.mark.parametrize('index', range(4))
def test_single_direction(index):
    assert main.init([pytest.directions[index]]) == [pytest.directions[index]]


def test_direction_1_path():
    assert main.init(pytest.direction_1) == []


def test_direction_2_path():
    assert main.init(pytest.direction_2) == ["WEST", "WEST"]


def test_direction_3_path():
    assert main.init(pytest.direction_3) == ["WEST"]


def test_direction_4_path():
    assert main.init(pytest.direction_4) == []


def test_direction_5_path():
    assert main.init(pytest.direction_5) == pytest.direction_5
