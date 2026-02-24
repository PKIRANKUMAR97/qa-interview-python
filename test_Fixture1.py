"""
The @pytest.fixture decorator is used in the Python testing framework pytest to define functions that manage test dependencies, state, and can include setup and teardown logic.
Pytest fixtures are a powerful feature that allows you to set up and tear down resources needed for your tests.
They help in creating reusable and maintainable test code.
A Fixture is a piece of code that runs and returns output before the execution of each test
The fixtures help the user to use the certain part of code just by declaring and reading it once, thus it becomes a crucial part of Pytest.


https://www.geeksforgeeks.org/python/fixtures-in-pytest/

"""

import pytest
import math
@pytest.fixture
def input_value():
    value = 9
    return value

# using fixture in test

def test_difference(input_value):
    assert 100-91 == input_value

def test_addition(input_value):
    assert 8 + 1 == input_value



