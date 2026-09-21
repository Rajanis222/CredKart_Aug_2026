from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Login_Page_Class:
    text_email_ID="email"
    text_password_Id="password"
    button_login_class_name="btn-primary"
    link_menubutton_xpath="//a[@role='button']"
    link_logout_xpath="//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver=driver

    def enter_email(self,email):
        self.driver.find_element(By.ID,self.text_email_ID).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(By.ID,self.text_password_Id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CLASS_NAME,self.button_login_class_name).click()

    def click_menu(self):
        self.driver.find_element(By.XPATH,self.link_menubutton_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH,self.link_logout_xpath).click()

    def verify_menu(self):
        try:
            WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[@role='button']")))
            return "Pass"
        except:
            return "Fail"




