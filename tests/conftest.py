import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory


@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")

@pytest.fixture(scope='class')
def oneTimeSetUp(request, browser):
    print('Running one time setUp')
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    # if browser == 'firefox':
    #     baseURl = 'https://courses.letskodeit.com/'
    #     driver = webdriver.Edge()
    #     driver.maximize_window()
    #     driver.implicitly_wait(2)
    #     driver.get(baseURl)
    #     print("Running tests on Firefox")
    # elif browser == 'chrome':
    #     baseURl = 'https://courses.letskodeit.com/'
    #     driver = webdriver.Chrome()
    #     driver.maximize_window()
    #     driver.implicitly_wait(2)
    #     driver.get(baseURl)
    #     print("Running tests on Chrome")
    # else:
    #     baseURl = 'https://courses.letskodeit.com/'
    #     driver = webdriver.Edge()
    #     driver.maximize_window()
    #     driver.implicitly_wait(2)
    #     driver.get(baseURl)
    #     print("Running tests on Edge")
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print('Running one time tearDown')

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help='Type of operating system')

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")