class CreateTransaction():
    def __init__(self,driver):
        self.driver = driver

        self.create_tran_button_xpath = "//button[@class='MuiButtonBase-root MuiIconButton-root']//*[@class='MuiSvgIcon-root']"
        self.description_testField_xpath = "//input[@name='description']"
        self.category_dropdown_xpath = "//div[contains(@class,'css-1hwfws3')]"
        self.select_category_xpath_mortgage = "//div[contains(text(),'Mortgage')]"
        self.enter_amount_textfield_xpath = "//input[@name='amount']"
        self.select_date_xpath = "//input[@name='createdAt']"
        self.save_button_xpath = "//span[contains(text(),'Save')]"
        self.select_category_xpath_car = "//div[contains(text(),'Car')]"

    def click_new_transaction(self):
        self.driver.find_element_by_xpath(self.create_tran_button_xpath).click()

    def enter_description(self,description):
        self.driver.find_element_by_xpath(self.description_testField_xpath).send_keys(description)

    def click_category(self):
        self.driver.find_element_by_xpath(self.category_dropdown_xpath).click()

    def select_mortgage(self):
        self.driver.find_element_by_xpath(self.select_category_xpath_mortgage).click()

    def select_car(self):
        self.driver.find_element_by_xpath(self.select_category_xpath_car).click()

    def enter_amount(self,amount):
        self.driver.find_element_by_xpath(self.enter_amount_textfield_xpath).send_keys(amount)

    def enter_date_transaction(self,transactiondate):
        self.driver.find_element_by_xpath(self.select_date_xpath).send_keys(transactiondate)

    def click_save_button(self):
        self.driver.find_element_by_xpath(self.save_button_xpath).click()






