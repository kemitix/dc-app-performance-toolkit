from .basePage import BasePage
from .pageElements import PageElement


class ProjectPage(BasePage):

    PROJECT_TITLE = PageElement.by_css_selector(".jira-project-avatar")
    PROJECT_SETTINGS = PageElement.by_css_selector(".aui-sidebar-settings-button")

    @property
    def project_title(self):
        avatar = self.find_element(self.PROJECT_TITLE)
        return avatar.get_attribute("title")

    def delete_project(self):
        self.click(self.PROJECT_SETTINGS)
        self.click(PageElement.by_css_selector("#view_delete_project"))
        self.click(PageElement.by_css_selector('#delete-project-confirm-submit'))
        # wait for Acknowledge button
        self.click(PageElement.by_css_selector("#acknowledge-submit"))