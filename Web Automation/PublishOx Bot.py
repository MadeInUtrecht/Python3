from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys
from selenium.webdriver.support.ui import WebDriverWait

def waitForLoad(inputXPath):
    Wait = WebDriverWait(driver, 10)
    Wait.until(EC.presence_of_element_located((By.XPATH, inputXPath)))

def newest_post_clicker():
    post = driver.find_element_by_css_selector('#main > div.infinite-scroll > div:nth-child(1) > div.content')
    title = post.find_element_by_css_selector('h2 > a').text
    author = post.find_element_by_css_selector('p.text-secondary > small:nth-child(4) > a').text
    click_title = driver.find_element_by_link_text(title)
    click_title.click()
    slider = driver.find_element_by_xpath('//*[@id="tipslider"]')

email = 'vadim-1@live.com'
password = 'Axwell29'
desired_url = 'https://www.publish0x.com/'
options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--window-size=1920,1080")
## options.add_argument("user-data-dir=/Users/vadim/Library/Application Support/BraveSoftware/Brave-Browser")
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
driver_path = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(options=options, executable_path=driver_path)
driver.get('https://www.publish0x.com/login')
waitForLoad('//*[@id="email"]')
E_Mail_vak = driver.find_element_by_xpath('//*[@id="email"]')
E_Mail_vak.send_keys(email)
Pass_vak = driver.find_element_by_xpath('//*[@id="password"]')
Pass_vak.send_keys(password)
frame = driver.find_element_by_xpath('//iframe[contains(@src, "recaptcha")]')
driver.switch_to.frame(frame)
Captcha = driver.find_element_by_xpath("//*[@id='recaptcha-anchor']")
Captcha.click()
wait = WebDriverWait(driver, 500)
# wait.until(EC.url_to_be("publish0x.com"))
def url_to_be(url):
    """An expectation for checking the current url.
    url is the expected url, which must be an exact match
    returns True if the url matches, false otherwise."""
    def _predicate(driver):
        return url == driver.current_url

    return _predicate

if url_to_be(desired_url) == True:
    driver.get('https://www.publish0x.com/newposts')
else:
    time.sleep(15)
    retry

newest_post_clicker()
def newest_post_clicker():
    post = driver.find_element_by_css_selector('#main > div.infinite-scroll > div:nth-child(1) > div.content')
    title = post.find_element_by_css_selector('h2 > a').text
    author = post.find_element_by_css_selector('p.text-secondary > small:nth-child(4) > a').text
    click_title = driver.find_element_by_link_text(title)
    click_title.click()
    slider = driver.find_element_by_xpath('//*[@id="tipslider"]')