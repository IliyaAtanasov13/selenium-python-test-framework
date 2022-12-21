from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as ExpectedConditions
import utilities.custom_logger as cl
import logging


class SeleniumDriver():
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        if locatorType == 'name':
            return By.NAME
        if locatorType == 'xpath':
            return  By.XPATH
        if locatorType == 'css':
            return By.CSS_SELECTOR
        if locatorType == 'class':
            return By.CLASS_NAME
        if locatorType == 'link':
            return By.LINK_TEXT
        if locatorType == 'partialink':
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.info('Locator type ' + locatorType + ' not correct/supported')
        return False

    def getElement(self, locator, locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info(f'Element found with locator {locator} and locatorType {locatorType}.')
        except:
            self.log.error(f'Element not found with locator {locator} and locatorType {locatorType}.')
        return element

    def isElementPresent(self, locator, locatorType='id'):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info(f"Element present with locator {locator} and locatorType {locatorType}.")
                return True
            else:
                self.log.error(f'Element not present with locator {locator} and locatorType {locatorType}.')
                return False
        except:
            self.log.error(f'Element not present with locator {locator} and locatorType {locatorType}.')
            return False

    def elementsPresenceCheck(self, locator, locatorType='xpath'):
        try:
            elementList = self.driver.find_elements(locatorType, locator)
            if len(elementList) > 0:
                self.log.info("Element found.")
                return True
            else:
                self.log.error('Element not found.')
                return False
        except:
            self.log.error('Element not found.')
            return False

    def elementClick(self, locator, locatorType='id'):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info(f'Clicked on element with locator {locator} locator type {locatorType}')
        except:
            self.log.error(f'Cannot click on the element with locator {locator} locator type {locatorType}')
            #print_stack()

    def sendKeys(self, data, locator, locatorType='xpath'):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info(f'Sent data on element with locator {locator} locator type {locatorType}')
        except:
            self.log.error(f'Cannot send data on element with locator {locator} locator type {locatorType}')
            #print_stack()

    def waitForElement(self, locator, locatorType='id', timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info('Waiting for maximum ' + str(timeout)) + ' seconds for element to be clickable'
            wait = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException,
                                                                                        ElementNotVisibleException,
                                                                                        ElementNotSelectableException])
            element = wait.until(ExpectedConditions.element_to_be_clickable((byType, 'stopFilter_stops-0')))
            self.log.info(f'Element with locator {locator} locator type {locatorType} appeared on the web page')
        except:
            self.log.error(f'Element with locator {locator} locator type {locatorType} did not appeared on the web page')
            #print_stack()
        return element

    def getElementText(self, locator, locatorType='link'):
        try:
            element = self.getElement(locator, locatorType).text()
            self.log.info(f'Element text is stored - locator {locator} locator type {locatorType}')
            return element.text()
        except:
            self.log.error(f'Elemement text was not stored - locator {locator} locator type {locatorType}')

    def isEnabled(self, locator, locatorType="id", info=""):
        """
        Check if element is enabled

        Parameters:
            1. Required:
                1. locator - Locator of the element to check
            2. Optional:
                1. locatorType - Type of the locator(id(default), xpath, css, className, linkText)
                2. info - Information about the element, label/name of the element
        Returns:
            boolean
        Exception:
            None
        """
        element = self.getElement(locator, locatorType=locatorType)
        enabled = False
        try:
            attributeValue = self.getElementAttributeValue(element=element, attribute="disabled")
            if attributeValue is not None:
                enabled = element.is_enabled()
            else:
                value = self.getElementAttributeValue(element=element, attribute="class")
                self.log.info("Attribute value From Application Web UI --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is not enabled")
        except:
            self.log.error("Element :: '" + info + "' state could not be found")
        return enabled