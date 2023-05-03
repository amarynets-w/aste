import pytest


def test_always_passes():
    assert True


def test_always_fails():
    assert False


def test_check_common_fixture(common_fixture):
    assert 42 == common_fixture


def test_example_fixture_in_another_module(example_fixture):
    assert 1 == example_fixture


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
