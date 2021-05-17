import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from .navigator import Navigator
from .pages.dashboardPage import DashboardPage
from .pages.loginPage import LoginPage

PATH: str = "/home/pcampbell/bin/chromedriver"


class BaseTestCase(unittest.TestCase):

    driver: WebDriver
    navigator: Navigator

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(PATH)
        self.navigator = Navigator(self.driver)
        self.navigator.get("")

    def login(self) -> DashboardPage:
        login_page = LoginPage(self.driver)
        return login_page.login_as('admin', 'admin')