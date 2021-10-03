class SearchCustomer:
    link_customer_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    rd_customer_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    txt_email_id = 'SearchEmail'
    btn_search_id = 'search-customers'
    col_emailids_xpath = "//table[@id='customers-grid']/tbody/tr/td[2]"

    def __init__(self, driver):
        self.driver = driver

    def click_customerMain_link(self):
        self.driver.find_element_by_xpath(self.link_customer_xpath).click()

    def click_customer_rd(self):
        self.driver.find_element_by_xpath(self.rd_customer_xpath).click()

    def enter_emailid(self, emailID_input):
        self.driver.find_element_by_id(self.txt_email_id).send_keys(emailID_input)

    def click_search_btn(self):
        self.driver.find_element_by_id(self.btn_search_id).click()

    def verify_user(self, emailID_input):
        flag = False
        lst_emailIDs = self.driver.find_elements_by_xpath(self.col_emailids_xpath)
        for emailID in lst_emailIDs:
            actual_emailID = emailID.text
            if actual_emailID == emailID_input:
                flag = True
                break
            else:
                print("Email ID not found")





