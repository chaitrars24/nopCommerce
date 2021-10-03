import random
import string

from pageObjects.AddCustomer import AddCustomer
from pageObjects.LoginPage import LoginPage
import time

from utilities.readProperties import ReadConfig


class Test_001_AddCustomer:
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    custPassword = ReadConfig.getCustPassword()
    firstName = ReadConfig.getFirstName()
    lastName = ReadConfig.getLastName()
    gender = ReadConfig.getGender()
    monthInDOB = ReadConfig.getMonthInDOB()
    yearInDOB = ReadConfig.getYearInDOB()
    dayInDOB = ReadConfig.getDayInDOB()
    companyName = ReadConfig.getCompanyName()
    custRole = ReadConfig.getCustRoles()
    vendor = ReadConfig.getVendor()
    exp_message = ReadConfig.getValidationMessage()
    dob = ReadConfig.getDOB()

    def test_addCust(self, setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.set_email(self.email)
        self.lp.set_password(self.password)
        self.lp.click_login()
        print("clicked login")
        time.sleep(2)
        self.addCust = AddCustomer(self.driver)
        self.addCust.click_customerMain_link()
        time.sleep(2)
        self.addCust.click_customer_rd()
        time.sleep(2)
        self.addCust.click_addnew_btn()
        self.email = self.get_random_string() + '@gmail.com'
        print(self.email)
        self.addCust.set_email(self.email)
        self.addCust.set_password(self.custPassword)
        self.addCust.set_first_name(self.firstName)
        self.addCust.set_last_name(self.lastName)
        self.addCust.select_gender(self.gender)
        self.addCust.select_dob(self.dob)
        # self.addCust.select_dob(self.monthInDOB, self.yearInDOB, self.dayInDOB)
        self.addCust.set_companyName(self.companyName)
        self.addCust.select_tax()
        # self.addCust.select_cust_role(self.custRole)
        self.addCust.select_vendor(self.vendor)
        self.addCust.click_save()
        self.addCust.verify_message(self.exp_message)

    def get_random_string(self):
        letters = string.ascii_lowercase + string.digits
        self.result_str = ''.join(random.choice(letters) for i in range(6))
        return self.result_str




