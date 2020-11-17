from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime

day = datetime.datetime.now()
dag = day.weekday()
def Testing():
    if dag >= 5:
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument("--window-size=1920,1080")
        options.add_argument("/Users/vadim/Library/Application Support/BraveSoftware/Brave-Browser")
        options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
        driver_path = '/usr/local/bin/chromedriver'
        driver = webdriver.Chrome(options=options, executable_path=driver_path)
        driver.get('https://outlook.live.com/mail/0/inbox')
        Outlook_Aanmelden = driver.find_element_by_xpath('/html/body/header/div/aside/div/nav/ul/li[2]/a')
        Outlook_Aanmelden.click()
        Email_Field = driver.find_element_by_xpath('//*[@id="i0116"]')
        Email_Field.send_keys('vadim-1@live.com')
        Outlook_Volgende = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
        Outlook_Volgende.click()
        time.sleep(0.5)
        Password_Field = driver.find_element_by_xpath('//*[@id="i0118"]')
        Password_Field.send_keys('Fakdapolice1!')
        Password_Field.send_keys(Keys.ENTER)
        Inlog_Outlook = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
        Inlog_Outlook.click()
        driver.execute_script("window.open('https://youtube.com');")
        return driver
    else:
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument("--window-size=1920,1080")
        options.add_argument("/Users/vadim/Library/Application Support/BraveSoftware/Brave-Browser")
        options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
        driver_path = '/usr/local/bin/chromedriver'
        driver = webdriver.Chrome(options=options, executable_path=driver_path)
        driver.get('https://outlook.live.com/mail/0/inbox')
        Outlook_Aanmelden = driver.find_element_by_xpath('/html/body/header/div/aside/div/nav/ul/li[2]/a')
        Outlook_Aanmelden.click()
        Email_Field = driver.find_element_by_xpath('//*[@id="i0116"]')
        Email_Field.send_keys('vadim-1@live.com')
        Outlook_Volgende = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
        Outlook_Volgende.click()
        time.sleep(0.5)
        Password_Field = driver.find_element_by_xpath('//*[@id="i0118"]')
        Password_Field.send_keys('Fakdapolice1!')
        Password_Field.send_keys(Keys.ENTER)
        Inlog_Outlook = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
        Inlog_Outlook.click()
        driver.execute_script("window.open('https://youtube.com');")
        return driver
Testing()