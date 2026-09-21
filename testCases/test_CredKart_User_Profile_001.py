import logging

from faker import Faker
import pytest
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.Login_Page import Login_Page_Class
from pageObjects.Registration_Page import Registration_Page_Class
from utilities.Read_Config import ReadConfigClass
from utilities.Logger import log_generator_class

@pytest.mark.usefixtures("browser_setup")
class Test_User_Profile:
    driver=None
    homepage_url=ReadConfigClass.get_home_url()
    email=ReadConfigClass.get_data_for_email()
    password=ReadConfigClass.get_data_for_password()
    login_url=ReadConfigClass.get_login_url()
    Registartion_url=ReadConfigClass.get_registeration_url()
    log=log_generator_class.log_generation_method() # we will only get method name in logfile.
    logger=logging.getLogger("Test_User_Profile")  # to get class name instead of root in report and logs

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.flaky(reruns=1,reruns_delay=1)
    @pytest.mark.dependency(name="test_credkart_url_001")
    def test_credkart_url_001(self):
        # self.driver.get("https://automation.credence.in")
        self.logger.info("Testcase test_credkart_url_001 is started ")
        self.driver.get(self.homepage_url)
        self.logger.info((f"Opening URL and landing on :{self.homepage_url}"))
        self.logger.info("Checking page title")
        if self.driver.title=="CredKart":
            self.logger.info(f"Page title is correct and landed on {self.homepage_url} ")
            print("You are landed on correct page")
            self.logger.info("Taking screenshot")
            self.driver.save_screenshot(".\\screenshots\\credkart homepage_pass.png")
            self.logger.info("Testcase test_credkart_url_001 is Pass")
        else:
            self.logger.info(f"Page title is incorrect and landed on URL:{self.driver.title}")
            self.logger.info("Taking screenshot")
            self.driver.save_screenshot(".\\screenshots\\credkart homepage_fail.png")
            self.logger.info("Testcase test_credkart_url_001 is Fail")
            assert False
        self.logger.info("Testcase test_credkart_url_001 is completed")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.user_profile
    def test_credkart_login_002(self):
        # self.driver.get("https://automation.credence.in/login")
        self.log.info("Testcase test_credkart_login_002 is started ")
        self.driver.get(self.login_url)
        self.log.info(f"Opening browser and landing on:{self.login_url}  ")
        self.lp=Login_Page_Class(self.driver)

        # Enter email
        # email=self.driver.find_element(By.ID,"email")
        # email.send_keys("CredenceTest_5005@credence.in")
        # self.lp.enter_email("CredenceTest_5005@credence.in")
        self.log.info(f"Entering email:{self.email}")
        self.lp.enter_email(self.email)

        # Enter password
        # password=self.driver.find_element(By.ID,"password")
        # password.send_keys("Password@123")
        # self.lp.enter_password("Password@123")
        self.log.info("Entering password")
        self.lp.enter_password(self.password)

        # Click login button
        # login_button=self.driver.find_element(By.CLASS_NAME, "btn-primary")
        # login_button.click()
        self.log.info("Clicking on login button")
        self.lp.click_login()

        # try:
        #     WebDriverWait(self.driver,5).until(
        #         expected_conditions.visibility_of_element_located((By.XPATH,"//a[@role='button']"))
        #     )
        #     self.driver.save_screenshot(".\\Screenshots\\Login success screenshot.png")
        #     self.driver.find_element(By.XPATH,"//a[@role='button']").click()
        #     self.driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()
        #     print("Login Success")
        # except:
        #     self.driver.save_screenshot(".\\Screenshots\\Login fail screenshot.png")
        #     print("Login failed")
        #     assert False
        self.log.info("Checking login status")
        if self.lp.verify_menu()=="Pass":
            self.log.info("Login pass")
            self.log.info("clicking on menu button")
            self.lp.click_menu()
            self.log.info("Clicking on logout button")
            self.lp.click_logout()
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\User_Login_pass.png")
            self.log.info("Testcase test_credkart_login_002 is passed")
        else:
            self.log.info("Login fail")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\User_Login_fail.png")
            self.log.info("Testcase test_credkart_login_002 failed")
            assert False
        self.log.info("Testcase test_credkart_login_002 is completed")

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.user_profile
    def test_credkart_registration_003(self):
        # self.driver.get("https://automation.credence.in/register")
        self.log.info("Testcase test_credkart_registration_003 is started")
        self.driver.get(self.Registartion_url)
        self.log.info(f"Opening the browser and landing on:{self.Registartion_url}")
        name_data=Faker().name()
        email_data=Faker().email()

        self.rp=Registration_Page_Class(self.driver)
        self.lp=Login_Page_Class(self.driver)
        self.log.info((f"Entering name:{name_data}"))
        self.rp.enter_name(name_data)
        self.log.info(f"Entering email:{email_data}")
        self.lp.enter_email(email_data)
        # self.lp.enter_password("Password@123")
        self.log.info("Entering password")
        self.lp.enter_password(self.password)
        # self.rp.enter_confirm_password("Password@123")
        self.log.info("Entering confirm_password")
        self.rp.enter_confirm_password(self.password)
        self.log.info(("Clicking on register button"))
        self.rp.click_register()
        self.log.info("Checking registration status")
        if self.lp.verify_menu()=='Pass':
            self.log.info("Registration passed")
            self.log.info("Clicking on menu button")
            self.lp.click_menu()
            self.log.info("Clicking on logout button")
            self.lp.click_logout()
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\User_Registration Pass.png")
            self.log.info("Test case test_credkart_registration_003 is passed ")
        else:
            self.log.info("Registration failed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(",\\Screenshot\\User_Registartion Fail.png")
            self.log.info("Test case test_credkart_registration_003 is failed")
            assert False
        self.log.info("Testcase test_credkart_registration_003 is completed")









# pytest -v -s -n auto --html=HTMLReports/my_report.html --browser='chrome'
# pytest -v -s -n auto --alluredir="AllureReports" --browser='chrome'






