import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.courses.login_page import LoginPage
from pages.courses.register_courses_page import RegisterCoursePage
from pages.courses.buy_page import BuyPage
from pages.courses.enroll_JS_page import EnrollJSPage
import unittest
import pytest
from base.selenium_driver import SeleniumDriver
from ddt import ddt, data, unpack
from utilities.read_data import getCSVdata


@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
@ddt
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.loginPage = LoginPage(self.driver)
        self.selenium_driver = SeleniumDriver(self.driver)
        self.registerCourses = RegisterCoursePage(self.driver)
        self.buyPage = BuyPage(self.driver)
        self.enrollPage = EnrollJSPage(self.driver)

    @pytest.mark.run(order=1)
    @data(('dfgdf@sdf.com', 'Dtn0nline1*'),
          ('iaatanasov13@gmail.com', 'sdgd'))
    @unpack
    def test_invalid_login(self, email, password):
        self.loginPage.LogIn(email=email, password=password)
        self.selenium_driver.waitForElement(self.loginPage._login_error, locatorType='xpath')
        while self.loginPage.locateErrorLogin() is False:
            try:
                self.loginPage.LogIn(email=email, password=password)
                self.selenium_driver.waitForElement(self.loginPage._login_error, locatorType='xpath')

                assert self.loginPage.locateErrorLogin() is True
            except:
                pass

    @pytest.mark.run(order=2)
    @data(('iaatanasov13@gmail.com', 'Dtn0nline1*'))
    @unpack
    def test_valid_login(self, email, password):
        self.loginPage.LogIn(email=email, password=password)
        assert self.loginPage.locateAvatarIcon() is True

    @pytest.mark.run(order=3)
    # @data(('JavaScript for beginners', '0000 0000 0000 0000', '123', '08/24'),
    #       ('Selenium WebDriver With Java', '1111 1111 1111 1111', '123', '08/24'),
    #       ('Selenium WebDriver Advanced', '2222 2222 2222 2222', '123', '08/24'))
    # the path bellow can be provided with just the name of the file since it's located in the project folder
    # however it's good to provided the full path since the file can be located anywhere
    @data(*getCSVdata('C:\\Users\\iatan\\workspace_python\\pythonProject\\letsCodeIt\\test_data.csv'))
    @unpack
    def test_buy_JS_course_error(self, course, card_number, cvv_number, exp_date):
        self.registerCourses.selectCourse(course=course)
        self.enrollPage.clickEnrollButton()
        self.buyPage.enterCardInfo(card_number=card_number, exp_date=exp_date, cvv_number=cvv_number)
        self.buyPage.verifyBuyIsDisabled()
        self.registerCourses.clickAllCourses()

        # Select the iframe
        #self.driver.execute_script('arguments[0].scrollIntoView(true);', iframe)

        # Enter card info and buy course
        # driver.execute_script('window.scrollBy(0, 1200)')

        # Buy course

        # Verify error message
