from selenium.webdriver.common.keys import Keys

class CreateAccount():
    def __init__(self,driver):
        self.driver = driver

        self.create_acc_button_xpath = "//span[@class='MuiIconButton-label']//*[@class='MuiSvgIcon-root']"
        self.institution_className = "css-19bqh2r"
        self.select_inst_xpath = "//div[contains(text(),'Tangerine')]"
        self.enter_acc_name_xpath = "//input[@name='name']"
        self.enter_opBalance_xpath = "//input[@name='openingBalance']"
        self.enter_date_xpath = "//input[@name='openingBalanceDate']"
        self.save_button_xpath = "//span[contains(text(),'Save')]"

    def click_createAc(self):
        self.driver.find_element_by_xpath(self.create_acc_button_xpath).click()

    def click_intName(self):
        self.driver.find_element_by_class_name(self.institution_className).click()

    def select_ins(self):
        self.driver.find_element_by_xpath(self.select_inst_xpath).click()

    def enter_name(self,name):
        self.driver.find_element_by_xpath(self.enter_acc_name_xpath).send_keys(name)

    def enter_openingBalance(self,openingBalance):
        self.driver.find_element_by_xpath(self.enter_opBalance_xpath).send_keys(Keys.BACK_SPACE)
        self.driver.find_element_by_xpath(self.enter_opBalance_xpath).send_keys(openingBalance)

    def enter_openingDate(self,date):
        self.driver.find_element_by_xpath(self.enter_date_xpath).send_keys(date)

    def click_save_button(self):
        self.driver.find_element_by_xpath(self.save_button_xpath).click()












