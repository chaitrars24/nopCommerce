import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
base_url = ReadConfig.getBaseUrl()
email = ReadConfig.getEmail()
password = ReadConfig.getPassword()

@pytest.fixture()
def setup(browser):
    options = Options()

    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:\\Users\\Chaitra\\drivers\\chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="C:\\Selenium\\Drivers\\geckodriver.exe")
    elif browser == 'edge':
        driver = webdriver.Edge(executable_path="C:\\Users\\Chaitra\\drivers\\msedgedriver.exe")
    else:
        driver = webdriver.Chrome(executable_path="C:\\Users\\Chaitra\\drivers\\chromedriver.exe")

    driver.get(base_url)
    driver.maximize_window()
    lp = LoginPage(driver)
    driver.implicitly_wait(4)
    lp.set_email(email)
    lp.set_password(password)
    lp.click_login()

    yield driver
    driver.close()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['Application Name'] = 'nop commerce'
    config._metadata['Tester'] = 'Chaitra'





