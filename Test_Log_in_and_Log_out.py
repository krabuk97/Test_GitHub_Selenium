import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def test_Log_in():
    # open GitHub's page
    driver.get("https://github.com/login")

    # find elements for login and password
    Login = driver.find_element(By.ID, "login_field")
    Password = driver.find_element(By.ID,"password")

    # Enter Login and password in empty field and press "Sign in"
    Login.send_keys("ruslancheberdin@gmail.com")
    Password.send_keys("Dumka040404")

    button_Sign_in = driver.find_element(By.NAME,"commit")
    button_Sign_in.click()

    # Now we press "Log out"
    Menu = driver.find_element(By.CLASS_NAME, "dropdown-caret")
    Menu.click()

    #Log_out = driver.find_element(By.CSS_SELECTOR, 'button.Header-link.btn-link[data-analytics-event*="sign out"]')
    #Log_out.click()

    time.sleep(5)

test_Log_in()
