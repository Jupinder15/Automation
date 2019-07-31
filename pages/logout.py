class Logout():
    def __init__(self,driver):
        self.driver = driver

        self.guest_user_button_xpath = "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-colorInherit']"
        self.logout_xpath = "//li[@class='MuiButtonBase-root MuiListItem-root MuiMenuItem-root MuiMenuItem-gutters MuiListItem-gutters MuiListItem-button']"

    def click_guestUser_button(self):
        self.driver.find_element_by_xpath(self.guest_user_button_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_xpath).click()

