class HomePage():
    def __init__(self,driver):
        self.driver = driver

        self.test_drive_button_xpath = "//span[contains(text(),'Take it for a test drive')]"

    def click_testDrive_button(self):
        self.driver.find_element_by_xpath(self.test_drive_button_xpath).click()