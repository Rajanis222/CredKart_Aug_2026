import logging

from faker import Faker
import pytest
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.Login_Page import Login_Page_Class
from pageObjects.Registration_Page import Registration_Page_Class
from utilities import Excel_Utils
from utilities.Read_Config import ReadConfigClass
from utilities.Logger import log_generator_class

@pytest.mark.usefixtures("browser_setup")
class Test_User_Login_002:
    driver=None
    home_page_url=ReadConfigClass.get_home_url()
    registration_url=ReadConfigClass.get_registeration_url()
    login_url=ReadConfigClass.get_login_url()
    log=log_generator_class.log_generation_method()

    def test_Credkart_Login_params_004(self,credkart_login_data):
        self.log.info("Testcase test_Credkart_Login_params_004 is started")
        self.driver.get(self.login_url)
        self.log.info(f"Opening browser and landing on {self.login_url} ")
        self.lp=Login_Page_Class(self.driver)
        self.email=credkart_login_data[0]
        self.password=credkart_login_data[1]
        self.expected_result=credkart_login_data[2]
        self.log.info("Entering password")
        self.lp.enter_email(self.email)
        self.log.info("Entering password")
        self.lp.enter_password(self.password)
        self.log.info("Clicking on login button")
        self.lp.click_login()
        self.log.info("Checking login status")
        if self.lp.verify_menu()=="Pass":
            self.log.info("Login pass")
            self.log.info("Click on menu button")
            self.lp.click_menu()
            self.log.info("Click on logout menu")
            self.lp.click_logout()
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\User_Login_pass_{self.email}.png")
            self.log.info("Testcase test Credkart_Login_params_004 passed ")
            actual_result="login_pass"
        else:
            self.log.info("Login fail")
            self.log.info(f"Taking screenshot for login fail")
            self.driver.save_screenshot(f".\\Screenshots\\User_Login_fail_{self.email}.png")
            self.log.info("Testcase test_Credkart_login_params_004 is failed")
            actual_result = 'login_fail'

        assert actual_result==self.expected_result,f"{actual_result}!={self.expected_result}"
        self.log.info("Testcase test_Credkart_login_params_004 is completed")

    def test_Credkart_Login_excel_005(self):
        excel_path=".\\TestData\\Test_Data.xlsx"
        sheet_name="Login_Data"
        self.log.info("Testcase test_Credkart_Login_excel_005 is started")
        self.lp = Login_Page_Class(self.driver)

        self.rows = Excel_Utils.row_count(excel_path, sheet_name)
        print(f"Number of rows in excel sheet->{self.rows}")
        result_list=[]

        for i in range(2,self.rows+1):
            self.driver.get(self.login_url)
            self.log.info(f"Opening browser and landing on {self.login_url} ")
            self.email=Excel_Utils.read_data(excel_path,sheet_name,i,2)
            self.password=Excel_Utils.read_data(excel_path,sheet_name,i,3)
            self.expected_result=Excel_Utils.read_data(excel_path,sheet_name,i,4)

            self.log.info("Entering Email")
            self.lp.enter_email(self.email)
            self.log.info("Entering password")
            self.lp.enter_password(self.password)
            self.log.info("Clicking on login button")
            self.lp.click_login()
            self.log.info("Checking login status")

            if self.lp.verify_menu()=="Pass":
                self.log.info("Login pass")
                self.log.info("Click on menu button")
                self.lp.click_menu()
                self.log.info("Click on logout menu")
                self.lp.click_logout()
                self.log.info("Taking screenshot")
                self.driver.save_screenshot(".\\Screenshots\\User_Login_pass_{self.email}.png")
                actual_result="login_pass"
            else:
                self.log.info("Login fail")
                self.log.info(f"Taking screenshot for login fail")
                self.driver.save_screenshot(f".\\Screenshots\\User_Login_fail_{self.email}.png")
                self.log.info("Testcase test_Credkart_login_excel_005 is failed")
                actual_result = 'login_fail'

            self.log.info("Writing data into excel file")
            Excel_Utils.write_data(excel_path,sheet_name,i,5,actual_result)
            if self.expected_result==actual_result:
                test_case_status="Pass"
            else:
                test_case_status = "Fail"
            result_list.append(test_case_status)
            Excel_Utils.write_data(excel_path,sheet_name,i,6,test_case_status)

            if "Fail" not in result_list:
                self.log.info(f"All testcases are passed")
                self.log.info("Testcase test Credkart_Login_excel_005 passed")
                assert True
            else:
                self.log.info(f"Some tesrcases are failed ")
                self.log.info("Testcase test Credkart_Login_excel_005 failed")
                assert False
            self.log.info("Testcase test_Credkart_Login_excel_005 is completed")


            # assert actual_result==self.expected_result,f"{actual_result}!={self.expected_result}"
            # self.log.info("Testcase test_Credkart_login_params_004 is completed")

# pytest -v -s -n=auto --html=HTMLReports/my_report.html --browser chrome -k "test_Credkart_Login_excel_005"
