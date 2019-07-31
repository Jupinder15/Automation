

# Write Automation test script to create an account and add two payments in it.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pytest
from pages.entaxyCreateAc import CreateAccount
from pages.EntaxyCreateTrans import CreateTransaction
from pages.homePage import HomePage
from pages.logout import Logout

class TestTransaction():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:\Python27\chromedriver_win32\chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()

    def test_transaction(self,test_setup):
        #navigate to this url
        driver.get("http://entaxy-staging.s3-website.ca-central-1.amazonaws.com/")

        #create objects for HomePage,CreateAccount and Create Transaction Classes
        home = HomePage(driver)                     # object of HomePage class
        account = CreateAccount(driver)             # object of createAccount class
        tran = CreateTransaction(driver)            # object of createTransaction class
        log = Logout(driver)

        #click on the 'Take it for a Test Drive' Button
        home.click_testDrive_button()

        #verify that we are on dashboard page
        title = driver.title
        if title=='Entaxy':
            print('we are on the dashboard')


        #create an account
        account.click_createAc()                    # click on the create account '+' button
        account.click_intName()                     # click on the institute name combo box
        account.select_ins()                        # select 'Tangerine' from there
        account.enter_name("Jupinder Singh")        # enter account name as 'Jupinder Singh'
        account.enter_openingBalance("2000")        # enter account balanse as '2000'
        account.enter_openingDate("07/29/2019")     # enter opening date as '07/29/2019'
        account.click_save_button()                 # click on save button

        #verify that the account is created successfull
        if driver.find_element_by_xpath("//h6[@class='MuiTypography-root MuiTypography-h6']"):
            print('Account Created successfully')


        # create a new transaction for rent (out transaction)
        tran.click_new_transaction()                # click on the new transaction '+' button on top right corner
        tran.enter_description("Rent")              # enter description as 'Rent'
        tran.click_category()                       # click on the category combo box
        tran.select_mortgage()                      # select 'Mortgage and Rent' from combo box
        tran.enter_amount("-500")                   # enter the amount as '-500'
        tran.enter_date_transaction("07/28/2019")   # enter the date as '07/28/2019'
        tran.click_save_button()                    # click the save button

        # verify that the first transaction is created under 'Mortgage & Rent' Category
        if driver.find_element_by_xpath("//span[contains(text(),'Mortgage & Rent')]"):
            print('Transaction created sucessfully')

        # wait for 5 seconds
        time.sleep(5)


        # create another transaction for Car payment ( out transaction )
        tran.click_new_transaction()                # click on the new transaction '+' button on top right corner
        tran.enter_description("Car")               # enter description as 'Rent'
        tran.click_category()                       # click on the category combo box
        tran.select_car()                           # select 'Mortgage and Rent' from combo box
        tran.enter_amount("-300")                   # enter the amount as '-500'
        tran.enter_date_transaction("07/28/2019")   # enter the date as '07/28/2019'
        tran.click_save_button()                    # click the save button

        # Verify that the second transaction is created under 'Car Insurance' Category
        if driver.find_element_by_xpath("//span[contains(text(),'Car nsurance')]"):
            print('Transaction created sucessfully')

        # log out from the account
        log.click_guestUser_button()                # click on the Guest User Button
        log.click_logout()                          # Click on the Log Out Button
