from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
def waitForLoad(inputXPath):
    Wait = WebDriverWait(driver, 10)
    Wait.until(EC.presence_of_element_located((By.XPATH, inputXPath)))
options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--headless")
## options.add_argument("user-data-dir=/Users/vadim/Library/Application Support/BraveSoftware/Brave-Browser")
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
driver_path = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(options=options, executable_path=driver_path)
driver.get('https://www.publish0x.com/login')
waitForLoad('//*[@id="email"]')
E_Mail_vak = driver.find_element_by_xpath('//*[@id="email"]')
E_Mail_vak.send_keys('vadim-1@live.com')
Pass_vak = driver.find_element_by_xpath('//*[@id="password"]')
Pass_vak.send_keys('Axwell29')
frame = driver.find_element_by_xpath('//iframe[contains(@src, "recaptcha")]')
driver.switch_to.frame(frame)
Captcha = driver.find_element_by_xpath("//*[@id='recaptcha-anchor']")
Captcha.click()
options.add_argument("--window-size=1920,1080")
Login_button = driver.find_element_by_xpath('//*[@id="login"]/div[4]/div/button')
Login_button.click()
