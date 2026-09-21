from selenium.webdriver.common.by import By
from pageObjects.Login_Page import Login_Page_Class


class Registration_Page_Class(Login_Page_Class):
    textbox_name_id="name"
    textbox_confirm_password_id="password-confirm"
    button_register_xpath="//button[normalize-space()='Register']"


    def __init__(self,driver):
        self.driver=driver

    def enter_name(self,name):
        self.driver.find_element(By.ID,self.textbox_name_id).send_keys(name)

    def enter_confirm_password(self,confirm_password):
        self.driver.find_element(By.ID,self.textbox_confirm_password_id).send_keys(confirm_password)

    def click_register(self):
        self.driver.find_element(By.XPATH,self.button_register_xpath).click()

