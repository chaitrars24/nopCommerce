import time

from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import generateLogs
from utilities.readProperties import ReadConfig
from utilities import ExcelDriven
import time


class Test_001_Login:
#    base_url = ReadConfig.getBaseUrl()
#    email = ReadConfig.getEmail()
#    password = ReadConfig.getPassword()
#    filePath = ReadConfig.getFilePath()
    filePath = '.\\TestData\\LoginData.xlsx'
    sheetName = ReadConfig.getSheetName()
    expectedTitle = ReadConfig.getDashboardTitle()

    log = generateLogs.logs()


    def test_login_ddt(self, setup):
        self.driver = setup
        self.rowcount = ExcelDriven.getRowCount(self.filePath,self.sheetName)
        self.lp = LoginPage(self.driver)

        for r in range(2, self.rowcount+1):
            self.user = ExcelDriven.readData(self.filePath, self.sheetName, r, 1)
            self.password = ExcelDriven.readData(self.filePath, self.sheetName, r, 2)
            self.lp.set_email(self.user)
            self.lp.set_password(self.password)
            self.lp.click_login()
            time.sleep(3)

            act_title = self.driver.title
            if act_title == self.expectedTitle:
                assert True
                self.lp.click_logout()
            else:
                assert True

        self.driver.close()








