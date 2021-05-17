import time

from .basePage import BasePage
from .pageElements import PageElement, Locator


class LoggedInPage(BasePage):

    __ADMIN_MENU = PageElement.by_css_selector("#admin_menu")
    __MANAGE_APPS_LINK = PageElement.by_css_selector("#admin_plugins_menu")
    __ADMIN_PROJECTS_MENU = PageElement.by_css_selector("#admin_project_menu")
    __TOOLBAR_CREATE_BUTTON = PageElement.by_css_selector("#create_link")
    __ISSUES_MENU = PageElement.by_css_selector("#find_link")
    __ISSUE_SEARCH_MENU = PageElement.by_css_selector("#issues_new_search_link_lnk")

    def click_manage_apps(self):
        self.click(self.__MANAGE_APPS_LINK)

    def click_admin_menu(self):
        self.click(self.__ADMIN_MENU)
        time.sleep(1)

    def click_admin_projects_menu(self):
        self.click(self.__ADMIN_PROJECTS_MENU)

    def click_toolbar_create_button(self):
        self.click(self.__TOOLBAR_CREATE_BUTTON)

    def custom_field_locator(self, field_id: str) -> Locator:
        return PageElement.by_css_selector(f"#customfield_{field_id}")

    def click_issue_menu(self):
        self.click(self.__ISSUES_MENU)

    def click_issue_search_menu(self):
        self.click(self.__ISSUE_SEARCH_MENU)
