from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time


class LoginPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    email = 'iaatanasov13@gmail.com'
    password = 'Dtn0nline1*'
    course = 'JavaScript'
    card_number = '0000 0000 0000 0000'
    cvv_number = '123'
    exp_date = '08/24'
    _iframe = '//form[@id="checkout-form"]//div[@class="panel payment-panel"]'
    _sign_in = "//div[@id='navbar-inverse-collapse']//a[@href='/login']"
    _login_button = '//div[@id="page"]/div[2]//input[@type="submit"]'
    _email = '//input[@id="email"and @placeholder="Email Address"]'
    _password = '//input[@id="password"]'
    _avatar_icon = 'dropdownMenu1'
    _login_error = '//div[@id="page"]//span[contains(text(), "Your username or password is invalid. Please try again.")]'
    login_error = 'Your username or password is invalid. Please try again.'
    _all_courses = '//div[@id="navbar-inverse-collapse"]//a[@href="/courses"]'
    _search_courses_field = "//form[@id='search']//input[@type='text']"
    _search_button = '//form[@id="search"]/div/button'
    _course = '//div[@id="course-list"]//a[@href="/courses/javascript-for-beginners"]'
    _enroll_button = "//*[@id='zen_cs_desc_with_promo_dynamic']//button[text()='Enroll in Course']"
    _card_num = "//div[@id='root']//input[@placeholder='Card Number']"
    _card_exp = "//div[@id='root']//input[@name='exp-date']"
    _card_cvv = "//div[@id='root']//input[@placeholder='Security Code']"
    _buy_button = "//form[@id='checkout-form']/div[2]/div[3]/div/div[1]/div[2]/div/button[1]"
    _enroll_error_message = "//li[@class='card-no cvc expiry text-danger']"

    def clickSignInLink(self):
        self.elementClick(self._sign_in, locatorType='xpath')

    def enterEmail(self, email):
     -    self.sendKeys(email, self._email, locatorType='xpath')

    def enterPassword(self, password):
        self.sendKeys(password, self._password, locatorType='xpath')

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType='xpath')

    def LogIn(self, email='', password=''):
        self.clickSignInLink()
        self.waitForElement(self._email, locatorType='xpath')
        self.waitForElement(self._password, locatorType='xpath')
        self.enterEmail(email)
        self.enterPassword(password)
        self.waitForElement(self._login_button, locatorType='xpath')
        self.clickLoginButton()

    def locateAvatarIcon(self):
        elementPresent = self.isElementPresent(self._avatar_icon)
        return elementPresent

    def verifySuccessfulLogin(self):
        assert self.locateAvatarIcon() is True

    def locateErrorLogin(self):
        errorPresent = self.isElementPresent(self._login_error, locatorType='xpath')
        return errorPresent

    def verifyFailedLogin(self):
        assert self.locateErrorLogin()
