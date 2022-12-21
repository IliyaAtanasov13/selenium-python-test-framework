import time
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class RegisterCoursePage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    course = 'JavaScript'
    card_number = '0000 0000 0000 0000'
    cvv_number = '123'
    exp_date = '08/24'
    email = 'iaatanasov13@gmail.com'
    password = 'Dtn0nline1*'
    _iframe = '//form[@id="checkout-form"]//div[@class="panel payment-panel"]'
    _sign_in = "//div[@id='navbar-inverse-collapse']//a[@href='/login']"
    _login_button = '//div[@id="page"]/div[2]//input[@type="submit"]'
    _email = '//input[@id="email"and @placeholder="Email Address"]'
    _password = '//input[@id="password"]'
    _all_courses = '//div[@id="navbar-inverse-collapse"]//a[@href="/courses"]'
    _search_courses_field = "//form[@id='search']//input[@type='text']"
    _search_button = '//form[@id="search"]/div/button'
    #_course = '//div[@id="course-list"]//a[@href="/courses/javascript-for-beginners"]'
    _course = "//div[@id='course-list']/div[1]//h4[contains(text(),'JavaScript for beginners')]"
    _enroll_button = "//*[@id='zen_cs_desc_with_promo_dynamic']//button[text()='Enroll in Course']"
    _card_num = "//div[@id='root']//input[@placeholder='Card Number']"
    _card_exp = "//div[@id='root']//input[@name='exp-date']"
    _card_cvv = "//div[@id='root']//input[@placeholder='Security Code']"
    _buy_button = "//form[@id='checkout-form']/div[2]/div[3]/div/div[1]/div[2]/div/button[1]"
    _enroll_error_message = "//li[@class='card-no cvc expiry text-danger']"
    _js_label = '//div[@id="course-list"]//h4[contains(text(), "JavaScript for beginners")]'

    def clickAllCourses(self):
        self.elementClick(self._all_courses, locatorType='xpath')

    def enterCourseName(self, data=''):
        self.sendKeys(data, self._search_courses_field, locatorType='xpath')

    def clickSearch(self):
        self.elementClick(self._search_button, locatorType='xpath')

    def clickCourse(self, course):
        self.elementClick(locator=course, locatorType='partialink')

    def selectCourse(self, course):
        self.clickAllCourses()
        self.enterCourseName(course)
        self.clickSearch()
        self.checkJsCourse()
        self.clickCourse(course)

    def checkJsCourse(self):
        result = self.isElementPresent(self._js_label, locatorType='xpath')
        assert result is True
