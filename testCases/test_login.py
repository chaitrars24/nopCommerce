from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import generateLogs
from utilities.readProperties import ReadConfig


class Test_001_Login:
#    base_url = ReadConfig.getBaseUrl()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    log = generateLogs.logs()

    def test_homePageTitle(self, setup):
        self.log.info("***** test_homePageTitle stated *********")
        self.driver = setup
#        self.driver.get(self.base_url)
        actual_title = self.driver.title
        if actual_title == "Your store. Login1":
            assert True
            self.driver.close()
            self.log.info("Test passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            assert False
            self.driver.close()
            self.log.error("Test failed -Text did not match")

    def test_login(self, setup):
        self.driver = setup
#        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.set_email(self.email)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.driver.close()


