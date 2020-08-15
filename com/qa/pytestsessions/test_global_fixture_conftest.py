import pytest

#Create a conftest.py file at Project folder location:
#/Users/Parihar08/PycharmProjects/SeleniumPythonSession/com/qa/pytestsessions
#Add the global fixture code to be used in the conftest.py file:

@pytest.mark.usefixtures("init_driver")
class Base_Test:
    pass

class Test_Google(Base_Test):

    def test_google_title(self):
        self.driver.get("http://www.google.com/")
        assert self.driver.title == 'Google'


    def test_google_url(self):
        self.driver.get("http://www.google.com/")
        assert self.driver.current_url == 'https://www.google.com/'
