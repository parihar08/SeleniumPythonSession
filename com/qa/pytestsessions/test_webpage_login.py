from selenium import  webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("http://www.google.com/")
    assert driver.title == 'Google'

    driver.quit()

def test_facebook():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("http://www.facebook.com/")
    assert driver.title == 'Facebook - Log In or Sign Up'

    driver.quit()

def test_instagram():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("http://www.instagram.com/")
    assert driver.title == 'Instagram'

    driver.quit()

def test_gmail():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("http://www.gmail.com/")
    assert driver.title == 'Gmail'

    driver.quit()

def test_rediff():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("http://www.rediff.com/")
    assert driver.title == 'Rediff.com: News | Rediffmail | Stock Quotes | Shopping'

    driver.quit()