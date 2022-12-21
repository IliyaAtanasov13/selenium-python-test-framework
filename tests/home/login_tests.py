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


@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.loginPage = LoginPage(self.driver)
        self.selenium_driver = SeleniumDriver(self.driver)
        self.registerCourses = RegisterCoursePage(self.driver)
        self.buyPage = BuyPage(self.driver)
        self.enrollPage = EnrollJSPage(self.driver)

    email = 'iaatanasov13@gmail.com'
    password = 'Dtn0nline1*'
    course = 'JavaScript'
    card_number = '0000 0000 0000 0000'
    cvv_number = '123'
    exp_date = '08/24'

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.loginPage.LogIn(self.email, 'sadfdsf')
        self.selenium_driver.waitForElement(self.loginPage._login_error, locatorType='xpath')
        while self.loginPage.locateErrorLogin() is False:
            try:
                self.loginPage.LogIn(self.email, 'sadfdsf')
                self.selenium_driver.waitForElement(self.loginPage._login_error, locatorType='xpath')

                assert self.loginPage.locateErrorLogin() is True
            except:
                pass

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.loginPage.LogIn(self.email, self.password)
        assert self.loginPage.locateAvatarIcon() is True

    @pytest.mark.run(order=3)
    def test_js_course(self):
        self.registerCourses.selectCourse(self.course)

    @pytest.mark.run(order=4)
    def test_buy_course_error(self):
        self.enrollPage.clickEnrollButton()
        self.buyPage.enterCardInfo(self.card_number, self.exp_date, self.exp_date)
        self.buyPage.verifyBuyIsDisabled()

        # Select the iframe
        #self.driver.execute_script('arguments[0].scrollIntoView(true);', iframe)

        # Enter card info and buy course
        # driver.execute_script('window.scrollBy(0, 1200)')

        # Buy course

        # Verify error message
