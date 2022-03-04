import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import adshopcart_locators as locators

#-----------------------------------------------------------

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
       driver.find_element(By.ID, "menuUser").click()
       sleep(2)
       assert driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').is_displayed()
       sleep(2)
       driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
       sleep(2)
       driver.find_element(By.CSS_SELECTOR, "[name='usernameRegisterPage']").send_keys(locators.new_username)
       sleep(5)
    # Click by the email,password open field and enter fake password
       driver.find_element(By.CSS_SELECTOR, "[name='emailRegisterPage']").send_keys(locators.email)
       driver.find_element(By.CSS_SELECTOR, "[name='passwordRegisterPage']").send_keys(locators.new_password)
       driver.find_element(By.CSS_SELECTOR, "[name='confirm_passwordRegisterPage']").send_keys(locators.new_password)
# Enter fake data into username open field
    driver.find_element(By.CSS_SELECTOR, "[name='first_nameRegisterPage']").send_keys(locators.first_name)
    driver.find_element(By.CSS_SELECTOR, "[name='last_nameRegisterPage']").send_keys(locators.last_name)
    driver.find_element(By.CSS_SELECTOR, "[name='addressRegisterPage']").send_keys(locators.address)
    driver.find_element(By.CSS_SELECTOR, "[name='postal_codeRegisterPage']").send_keys(locators.province)
    driver.find_element(By.CSS_SELECTOR, "[name='i_agree']").click()
    sleep(5)
    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep(5)
    driver.find_element(By.ID, "menuUser").click()
    sleep(5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[2]')
    print(f'user is registered')
    print(f'click by Account Menu')
    print(f'User fullname is displayed {locators.full_name}')
    sleep(2)


def home_page():
    if driver.current_url == locators.adshopcart_url:
        driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
        print(f'-------------------------------------------')
        print(f'Going to CONTACT US ')
        driver.find_element(By.NAME, 'SPEAKERS').is_displayed()
        sleep(1)
        driver.find_element(By.NAME, 'TABLETS').is_displayed()
        sleep(1)
        driver.find_element(By.NAME, 'HEADPHONES').is_displayed()
        sleep(1)
        driver.find_element(By.NAME, 'LAPTOPS').is_displayed()
        sleep(1)
        driver.find_element(By.NAME, 'MICE').is_displayed()
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'OUR PRODUCTS').click()
        sleep(1)
        driver.find_element(By.LINK_TEXT, 'SPECIAL OFFER').click()
        sleep(1)
        driver.find_element(By.LINK_TEXT, 'POPULAR ITEMS').click()
        print(f'These items are displayed & Clickable')
        sleep(2)
        if driver.page_source.find('dvantage'):
            print(f' Logo is dvantage ')
        else:
            print(f'Check your Code ')
            if driver.page_source.find('DEMO'):
                print(f'Logo DEMO,Displayed')
            else:
                print(f'Check the Error')
                sleep(2)


def Contact_Form():
    driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
    print(f'---------------------------------------------')
    print(f'Filling the CONTACT US FORM')
    sleep(2)
    Select(driver.find_element(By.XPATH, "//*@name='categoryListboxContactUs']")).select_by_visible_text('Laptops')
    sleep(2)
    Select(driver.find_element(By.XPATH,"//*[@name='productListboxContactUs']")).select_by_visible_text('HP chromebook14G1(ENERGY STAR')
    sleep(2)
    driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.email)
    sleep(2)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.description)
    sleep(2)
    driver.find_element(By.ID, 'Send_btnundefied').click()
    sleep(2)
    if driver.page_source.find('SPEAKERS'):
        print(f'We are good to go')
        print(f'Button is active')
    else:
        print(f'Check the Code')
        sleep(2)


def login():
    if driver.current_url==locators.adshopcart_url:
        driver.find_element(By.ID, "menuUser").click()
        sleep(1)
        driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
        sleep(1)
        driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
        sleep(1)
        driver.find_element(By.ID,'sign_in_btnundefined').click()
        print(f'User login')


def sign_out():
    if driver.current_url == locators.adshop_url:
        driver.find_element(By.ID, "menuUser").click()
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
        print(f'Log out successfully ')
        sleep(3)


def delete_account_login():
    driver.find_element(By.ID, "menuUser").click()
    sleep(1)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"My account")]').click()
    sleep(0.25)
    driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
    sleep(4)
    driver.find_element(By.XPATH, '//div[text()="yes"]').click()
    sleep(3)
    driver.find_element(By.ID, "menuUser").click()
    sleep(0.25)
    driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
    sleep(0.25)
    driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
    sleep(1)
    driver.find_element(By.ID, 'sign_in_btnudefined').click()
    sleep(1)
    if driver.find_element(By.ID, 'signInResultMessage'):
        print(f'-------------------------------------')
        print(f'User Account deleted succefully{locators.new_username}')
    else:
        print(f'Check the Code for Error')


setUp()
create_new_user()
delete_account_login()
sign_out()
login()
home_page()
Contact_Form()
tearDown()

