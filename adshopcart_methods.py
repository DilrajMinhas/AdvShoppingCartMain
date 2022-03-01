import datetime
from time import sleep
from selenium import webdriver
import adshopcart_locators as locators
from selenium.webdriver.chrome.service import Service

driver= webdriver.Chrome(r'C:\Users\hsmdilraj\PycharmProject\moodle\chromedriver.exe')

def setUp():
    print(f'Test started at: {datetime.datetime.now()}')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.adshopcart_url)
    if driver.current_url == locators.adshopcart_url and driver.title.endswith('Advantage Shopping'):
        print(f' The Web is page is visible {driver.current_url}')
        print(f'The title is {driver.title}')
    else:
        print(f' We are not at webpage')
        sleep(0.25)


def tearDown():
    if driver is not None:
        print (f'------------------')
        print(f'Test completed at:{datetime.datetime.now()}')
        sleep(5)
        driver.close()
        driver.quit()

#setUp()
#tearDown()
