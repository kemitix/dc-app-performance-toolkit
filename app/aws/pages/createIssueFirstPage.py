from .loggedInPage import LoggedInPage
from .pageElements import PageElement, PageFieldElement


class CreateIssueFirstPage(LoggedInPage):

    __PROJECT_FIELD = PageElement.by_css_selector('#project-single-select input')
    __ISSUE_TYPE_FIELD = PageElement.by_css_selector('#issuetype-single-select input')

    __project = PageFieldElement(__PROJECT_FIELD)
    __issue_type = PageFieldElement(__ISSUE_TYPE_FIELD)

    def next(self) -> None:
        self.submit(PageElement.by_css_selector("form#issue-create"))

    def set_project(self, project_key: str):
        self.click(PageElement.by_css_selector("#project-single-select > span"))
        if f"({project_key})" not in self.__project:
            self.click(PageElement.by_partial_link_text(f"({project_key})"))
        else:
            self.click(PageElement.by_css_selector("#project-single-select > span"))

    def set_issue_type(self, issue_type: str):
        self.click(PageElement.by_css_selector("#issuetype-single-select > span"))
        if issue_type not in self.__issue_type:
            self.click(PageElement.by_link_text(issue_type))
        else:
            self.click(PageElement.by_css_selector("#issuetype-single-select > span"))
