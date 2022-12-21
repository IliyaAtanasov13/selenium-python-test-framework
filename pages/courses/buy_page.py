import time

from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class BuyPage(SeleniumDriver):
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
    _course = '//div[@id="course-list"]//a[@href="/courses/javascript-for-beginners"]'
    _enroll_button = "//*[@id='zen_cs_desc_with_promo_dynamic']//button[text()='Enroll in Course']"
    _card_num = "//div[@id='root']//input[@placeholder='Card Number']"
    _card_exp = "//div[@id='root']//input[@name='exp-date']"
    _card_cvv = "//div[@id='root']//input[@placeholder='Security Code']"
    _buy_button = "//form[@id='checkout-form']/div[2]/div[3]/div/div[1]/div[2]/div/button[1]"
    _enroll_error_message = "//li[@class='card-no cvc expiry text-danger']"

    def getErrorMessage(self):
        message = self.driver.find_element(By.XPATH, self._enroll_error_message).text()
        # should check if the element is enabled or not bc it may be found but disabled at the same time
        return message

    def enterCardNumber(self, card_number):
        self.driver.switch_to.frame(0)
        self.sendKeys(card_number, self._card_num, locatorType='xpath')
        self.driver.switch_to.default_content()

    def enterExpDate(self, exp_date):
        self.driver.switch_to.frame(1)
        self.sendKeys(exp_date, self._card_exp, locatorType='xpath')
        self.driver.switch_to.default_content()

    def enterCvv(self, cvv_number):
        self.driver.switch_to.frame(2)
        self.sendKeys(cvv_number, self._card_cvv, locatorType='xpath')
        self.driver.switch_to.default_content()

    def clickBuyButton(self):
        self.elementClick(self._buy_button, locatorType='xpath')

    def enterCardInfo(self, card_number, exp_date, cvv_number):
        self.driver.execute_script('window.scrollBy(0, 700)')
        self.waitForElement(self._card_num, locatorType='xpath')
        self.enterCardNumber(card_number)
        self.enterExpDate(exp_date)
        self.enterCvv(cvv_number)

    def verifyBuyIsDisabled(self):
        enabled = self.isEnabled(self._buy_button, locatorType='xpath', info='Buy button')
        assert enabled is not True

    # not used in verify error message since it cannot be clicked on (the button is disabled)
    def buyCourse(self, card_number='', exp_date='', cvv_number=''):
        self.enterCardInfo(card_number, exp_date, cvv_number)
        self.clickBuyButton()

    # not used since the message is shown as soon as the user enters invalid card AND the Buy button is disabled
    def verifyErrorMessage(self, error='Your card number is incorrect.'):
        self.waitForElement(self._enroll_error_message, locatorType='xpath')
        assert self.getErrorMessage == error
