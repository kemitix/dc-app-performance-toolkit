from util.conf import BaseAppSettings
from .navigator import Navigator


def test_1_aws_opsitems(jsm_webdriver):

    navigator = Navigator(jsm_webdriver)

    def test_navigator_login():
        navigator.login()

    test_navigator_login()

    # def test_1_2_navigator_admin_projects_page(self):
    #     self.navigator.admin_projects_page()

    # def test_navigator_manage_apps_page(self):
    #     self.navigator.manage_apps_page()
    #
    # def test_navigator_account_list_page(self):
    #     self.navigator.account_list_page()
    #
    # def test_navigator_connector_setting_page(self):
    #     self.navigator.connector_settings_page()

    # def test_ops_items_create_and_resolve(self):
    #     """create an ops item issue and resolve it"""
        # self.navigator.login()
        # issue_key = self.navigator.create_ops_item(
        #     project=self.project_key,
        #     summary="new ops item",
        #     description="ops item description",
        #     severity="4 - Low",
        #     category="Performance",
        #     region="eu-central-1")
        # self.navigator.resolve_issue(issue_key)

    # def test_ops_item_find_and_mark_in_progress(self):
    #     """Search for any open OpsItem issue and mark as in progress"""
    #     issue_key = self.navigator.find_open_ops_item(self.project_key)
    #     self.navigator.in_progress_issue(issue_key)

    # def test_securityhub(self):
    #     page = self.navigator.login()
    #     # select aws project
    #     # view issues
    #     # filter to security findings
    #     # select first finding
    #     # add comment

