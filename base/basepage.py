import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.courses.register_courses_page import Tests
from utilities.utils import Utils


class BasePage(Tests):

    # Start Edge Browser in max size
    def startEdgeBrowser(self, baseUrl):
        driver = webdriver.Edge()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)

    # Click on the sing in button to go to the login page
    def signInButton(self, driver, _sign_in):
        signInButton = driver.find_element(By.XPATH, _sign_in)
        signInButton.click()



    # Go to All Courses
    def allCoursesButton(self, enterPass, driver, _all_courses):
        allCourses = driver.find_element(By.XPATH, _all_courses)
        allCourses.click()


    def enterCourseName(self, driver, course, _search_courses_field):
        searchCourseField = driver.find_element(By.XPATH, _search_courses_field)
        searchCourseField.send_keys(course)

