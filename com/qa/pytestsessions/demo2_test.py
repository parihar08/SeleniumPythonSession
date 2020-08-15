import pytest

def test_m4():
    assert False

def test_m5():
    assert 100 == 100

@pytest.mark.home
def test_m6():
    assert "Sandeep" == "sandeep"

@pytest.mark.login
def test_login():
    assert 'admin' == 'admin'