import pytest

def test_m1():
    a=3
    b=4
    assert a+1 ==b, "test failed"
    assert a==b, "test failed as a is not equal to b"

@pytest.mark.login
def test_m2():
    name='selenium'
    assert name.upper() == 'SELENIUM'

def test_m3():
    assert True

def test_login():
    assert 'admin' == 'admin'