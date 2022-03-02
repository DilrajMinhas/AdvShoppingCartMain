import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import adshopcart_locators as locators

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
        print(f'------------------')
        print(f'Test completed at:{datetime.datetime.now()}')
        sleep(5)
        driver.close()
        driver.quit()
def create_new_user():
    if driver.current_url==locators.adshopcart_url:
       driver.find_element(By.ID,"menuUser").click()
       sleep(5)
       assert driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').is_displayed()
       sleep(5)
       driver.find_element(By.LINK_TEXT,'CREATE NEW ACCOUNT').click()
       sleep(5)
       driver.find_element(By.CSS_SELECTOR,"[name='usernameRegisterPage']").send_keys(locators.new_username)
       sleep(5)
    # Click by the email,password open field and enter fake password
       driver.find_element(By.CSS_SELECTOR,"[name='emailRegisterPage']").send_keys(locators.email)
       driver.find_element(By.CSS_SELECTOR, "[name='passwordRegisterPage']").send_keys(locators.new_password)
       driver.find_element(By.CSS_SELECTOR,"[name='confirm_passwordRegisterPage']").send_keys(locators.new_password)
# Enter fake data into username open field
    driver.find_element(By.CSS_SELECTOR,"[name='first_nameRegisterPage']").send_keys(locators.first_name)
    driver.find_element(By.CSS_SELECTOR, "[name='last_nameRegisterPage']").send_keys(locators.last_name)
    driver.find_element(By.CSS_SELECTOR,"[name='addressRegisterPage']").send_keys(locators.address)
    driver.find_element(By.CSS_SELECTOR,"[name='postal_codeRegisterPage']").send_keys(locators.province)
    driver.find_element(By.CSS_SELECTOR,"[name='i_agree']").click()
    driver.find_element(By.ID,'register_btnundefined').click()
    print(f'user is registered')


setUp()
create_new_user()
tearDown()



#create_new_user()
