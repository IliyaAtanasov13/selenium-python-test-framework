import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.courses.register_courses_page import Tests


class Utils():


    def utils(self):

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
        # _courses = ""
        # _all_courses = ""
        _enroll_button = "//*[@id='zen_cs_desc_with_promo_dynamic']//button[text()='Enroll in Course']"
        _card_num = "//div[@id='root']//input[@placeholder='Card Number']"
        _card_exp = "//div[@id='root']//input[@name='exp-date']"
        _card_cvv = "//div[@id='root']//input[@placeholder='Security Code']"
        _buy_button = "//form[@id='checkout-form']/div[2]/div[3]/div/div[1]/div[2]/div/button[1]"
        _enroll_error_message = "//li[@class='card-no cvc expiry text-danger']"