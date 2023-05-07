import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from password import password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()


def test_log_in():
    # open GitHub's page
    driver.get("https://github.com/login")

    # find elements for login and password
    Login = driver.find_element(By.ID, "login_field")
    Password = driver.find_element(By.ID, "password")

    # Enter Login and password in empty field and press "Sign in"
    Login.send_keys("ruslancheberdin@gmail.com")
    Password.send_keys(password)

    button_Sign_in = driver.find_element(By.NAME, "commit")
    button_Sign_in.click()
    print("Test 1 Success!!!")


def new_repository():
    # Find new repository button
    new = driver.find_element(By.CLASS_NAME, "dropdown-caret")
    new.click()

    # Find and press new repository button
    newrep = driver.find_element(By.XPATH, '//a[@href="/new" and contains(@data-ga-click, "create new repository")]')
    newrep.click()

    # Create new repository
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "react-aria-2")))
    element.click()
    element.send_keys("TEST\n")

    text_field = driver.find_element(By.ID, "react-aria-3")
    text_field.send_keys("Repository for test")

    new_butt = driver.find_element(By.XPATH, "//button[@type='button' and @data-no-visuals='true']")
    new_butt.send_keys(Keys.ENTER)
    ActionChains(driver).move_to_element(new_butt).send_keys(Keys.ENTER).perform()
    time.sleep(5)
    print("Test 2 Success!!!")


def add_file_to_repository():
    # Open page our repository
    driver.get("https://github.com/krabuk97/TEST")

    # Click on add new file
    file_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@data-ga-click='Empty repo, click, Clicked create new file link']"))
    )
    file_link.click()

    # Enter name file "Test.txt" for example and press "Commit name"
    name_file = WebDriverWait(driver, 10).until(
       EC.presence_of_element_located((By.NAME, "filename"))
    )
    name_file.send_keys("Test.txt")

    new_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "submit-file"))
    )
    new_button.click()

    print("Test 3 Success!!!")
    time.sleep(5)


def browsing_test():
    # Open page our repository
    driver.get("https://github.com/krabuk97/TEST")

    # browse the contents of a repository on the GitHub page
    code = driver.find_element(By.ID, "code-tab")
    code.click()
    time.sleep(2)

    issues = driver.find_element(By.ID, "issues-tab")
    issues.click()
    time.sleep(2)

    pull = driver.find_element(By.ID, "pull-requests-tab")
    pull.click()
    time.sleep(2)

    actions = driver.find_element(By.ID, "actions-tab")
    actions.click()
    time.sleep(2)

    projects = driver.find_element(By.ID, "projects-tab")
    projects.click()
    time.sleep(2)

    wiki = driver.find_element(By.ID, "wiki-tab")
    wiki.click()
    time.sleep(2)

    security = driver.find_element(By.ID, "security-tab")
    security.click()
    time.sleep(2)

    insights = driver.find_element(By.ID, "insights-tab")
    insights.click()
    time.sleep(2)

    settings = driver.find_element(By.ID, "settings-tab")
    settings.click()
    time.sleep(5)


test_log_in()
new_repository()
add_file_to_repository()
browsing_test()
