import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from password import password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

def test_Log_in():
    # open GitHub's page
    driver.get("https://github.com/login")

    # find elements for login and password
    Login = driver.find_element(By.ID, "login_field")
    Password = driver.find_element(By.ID,"password")

    # Enter Login and password in empty field and press "Sign in"
    Login.send_keys("ruslancheberdin@gmail.com")
    Password.send_keys(password)

    button_Sign_in = driver.find_element(By.NAME,"commit")
    button_Sign_in.click()
    print("Test 1 Success!!!")


def new_repository():
    # Find new repository button
    new = driver.find_element(By.CLASS_NAME, "dropdown-caret")
    new.click()

    #Find and press new repository button
    newrep = driver.find_element(By.XPATH, '//a[@href="/new" and contains(@data-ga-click, "create new repository")]')
    newrep.click()

    #Create new repository
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "react-aria-2")))
    element.send_keys("TEST")
    create = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "Box-sc-g0xbh4-0 kkrdEu")))
    create.click()
    time.sleep(10)

    print("Test 2 Success!!!")

test_Log_in()
new_repository()