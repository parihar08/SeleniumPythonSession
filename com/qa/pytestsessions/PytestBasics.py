import pytest

#All the tests written should either start or end with test keyword
#Name of the file should also have Test keyword in the beginning or in the end

def test_m11():
    name='selenium'
    assert name.upper() == 'SELENIUM'

#To run a specific test -- py.test demo2_test.py
#To run all tests under a package -- py.test
#To run test with specific keyword e.g. login keyword -- py.test -k login -v