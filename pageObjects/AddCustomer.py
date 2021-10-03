import time

from selenium.webdriver.common.keys import Keys


class AddCustomer:

    link_customer_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    rd_customer_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    btn_AddNew_xpath = "//*[@href='/Admin/Customer/Create']"
    txt_email_xpath = "//input[@id='Email']"
    txt_password_xpath = "//input[@id='Password']"
    txt_firstname_xpath = "//input[@id='FirstName']"
    txt_lastname_xpath = "//input[@id='LastName']"
    lst_rb_gender_xpath = "//*[@class='form-check']/label"
    rb_male_xpath = "//*[@id='Gender_Male']"
    txt_dob_id = "DateOfBirth"
    btn_calender_xpath = "//*[@class='k-icon k-i-calendar']"
    btn_month_xpath = "//*[@class='k-link k-nav-fast']"
    lst_months_xpath = "//*[@role='row']/td/a"
    btn_calenderyear_xpath = "//*[@class='k-header']/a[2]"
    btn_calenderPrevious_xpath = "//*[@class='k-link k-nav-prev']"
    lst_years_xpath = "//*[@class='k-link']"
    lst_days_xpath = "//*[@role='gridcell']/a"
    txt_company_id = "Company"
    checkBox_tax_id = "IsTaxExempt"
    drp_customerRole_xpath = "(//*[@class='k-widget k-multiselect k-multiselect-clearable']/div)[2]"
    lst_customerRoles_xpath = "//ul[@id='SelectedCustomerRoleIds_listbox']/li"
    drp_vendor_id = "VendorId"
    lst_vendor_xpath = "//*[@id='VendorId']/option"
    btn_save_xpath = "//*[@name='save']"
    msg_validation_xpath = "//*[@class='alert alert-success alert-dismissable']"

    def __init__(self, driver):
        self.genderToSelect = 'Female'
        self.driver = driver

    def click_customerMain_link(self):
        self.driver.find_element_by_xpath(self.link_customer_xpath).click()

    def click_customer_rd(self):
        self.driver.find_element_by_xpath(self.rd_customer_xpath).click()

    def click_addnew_btn(self):
        self.driver.find_element_by_xpath(self.btn_AddNew_xpath).click()

    def set_email(self, email_id):
        self.driver.find_element_by_xpath(self.txt_email_xpath).send_keys(email_id)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.txt_password_xpath).send_keys(password)

    def set_first_name(self, firstname):
        self.driver.find_element_by_xpath(self.txt_firstname_xpath).send_keys(firstname)

    def set_last_name(self, lastname):
        self.driver.find_element_by_xpath(self.txt_lastname_xpath).send_keys(lastname)

    def select_gender(self, gender_input):
        self.driver.find_element_by_xpath(self.rb_male_xpath).click()
        genderList = self.driver.find_elements_by_xpath(self.lst_rb_gender_xpath)

        print(genderList)
        for gender in genderList:
            gender_value = gender.text
            if gender_value == gender_input:
                gender.click()
                break
            else:
                print("No match")

    def select_dob(self, dob_input):
        self.driver.find_element_by_id(self.txt_dob_id).send_keys(dob_input)


    # def select_dob(self, month_input, year_input, day_input, flag=True):
    #     self.driver.find_element_by_xpath(self.btn_calender_xpath).click()
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath(self.btn_month_xpath).click()
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath(self.btn_calenderyear_xpath).click()
    #     time.sleep(1)
    #     list_years = self.driver.find_elements_by_xpath(self.lst_years_xpath)
    #     for year in list_years:
    #         current_year = year.text
    #         print('currentyear', current_year)
    #         if current_year == year_input:
    #             year.click()
    #             True
    #             break
    #         while not flag:
    #             self.driver.find_element_by_xpath(self.btn_calenderPrevious_xpath).click()
    #             self.driver.implicitly_wait(10)
    #
    #
    #     list_months = self.driver.find_elements_by_xpath(self.lst_months_xpath)
    #     for month in list_months:
    #         monthName = month.text
    #         print(monthName)
    #         if monthName == month_input:
    #             month.click()
    #             break
    #     list_days = self.driver.find_elements_by_xpath(self.lst_days_xpath)
    #     for day in list_days:
    #         current_day = day.text
    #         if current_day == day_input:
    #             day.click()
    #             break


    def set_companyName(self, company_name):
        self.driver.find_element_by_id(self.txt_company_id).send_keys(company_name)

    def select_tax(self):
        self.driver.find_element_by_id(self.checkBox_tax_id).click()

#     def select_cust_role(self, role_input):
#
#         self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
#         time.sleep(2)
#         self.driver.find_element_by_xpath(self.drp_customerRole_xpath).click()
#         roles = self.driver.find_elements_by_xpath(self.lst_customerRoles_xpath)
#         for role in roles:
#             actual_role = role.text
#             print('roleinput ' + role_input)
#             print('actualrole ' + actual_role)
#             if actual_role == role_input:
#                 role.click()
#                 time.sleep(3)
# # self.driver.find_element_by_xpath("(//*[@class='k-widget k-multiselect k-multiselect-clearable']/div/input)[2]").click()
#                 drpClick = self.driver.find_element_by_xpath("(//*[@class='k-widget k-multiselect k-multiselect-clearable']/div/input)[2]")
#                 self.driver.execute_script("arguments[0].click();", drpClick)
#             else:
#                 pass

    def select_vendor(self, vendor_input):
        drp_vendor_click = self.driver.find_element_by_id(self.drp_vendor_id)
        drp_vendor_click.click()
        list_vendors = self.driver.find_elements_by_xpath(self.lst_vendor_xpath)
        for vendor in list_vendors:
            vendor_name = vendor.text
            if vendor_name == vendor_input:
                vendor.click()
                # drp_vendor_click.send_keys(Keys.TAB)
                break
            else:
                print("No match")

    def click_save(self):
        self.driver.find_element_by_xpath(self.btn_save_xpath).click()
        time.sleep(4)

    def verify_message(self, exp_message):
        actual_msg = self.driver.find_element_by_xpath(self.msg_validation_xpath).text
        if exp_message in actual_msg:
            assert True
        else:
            assert False

























