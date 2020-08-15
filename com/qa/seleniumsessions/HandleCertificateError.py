from selenium import webdriver
from selenium.webdriver import ActionChains,DesiredCapabilities
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec  #using alias
import time


#Certificate can be - Expired, Invalid, Self signed certificate, Parent certificate is not valid or expired
#To bypass using selenium in Google chrome
#1a. Use Options class using add arguments

#options = Options()
#options.add_argument('--allow-running-insecure-content')
#options.add_argument('--ignore-certificate-errors')

#driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

#1b. Use Options class using set capability
#options=Options()
#options.set_capability('acceptInsecureCerts',True)
#driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)

#2. Use Desired Capabilities

desired_capabilities = DesiredCapabilities().CHROME.copy()
desired_capabilities['acceptInsecureCerts'] =True

driver = webdriver.Chrome(ChromeDriverManager().install(),desired_capabilities=desired_capabilities)

driver.implicitly_wait(10)

driver.get("https:/expired.badssl.com/")

print(driver.find_element(By.TAG_NAME,'h1').text)

driver.quit()

# With Firefox

#1. Using Firefox profile
#profile = webdriver.FirefoxProfile()
#profile.accept_untrusted_certs =True
#driver1= webdriver.Firefox(executable_path=GeckoDriverManager().install(),firefox_profile=profile)

#2. Using Desired capabilities
desired_capabilities1= DesiredCapabilities.FIREFOX.copy()
desired_capabilities1['acceptInsecureCerts'] =True

driver1 = webdriver.Firefox(executable_path=GeckoDriverManager().install(),capabilities=desired_capabilities1)

driver1.implicitly_wait(10)

driver1.get("https:/expired.badssl.com/")

print(driver1.find_element(By.TAG_NAME,'h1').text)

driver1.quit()