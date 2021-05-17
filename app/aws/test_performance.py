from selenium_ui.conftest import print_timing
from .baseTestCase import BaseTestCase


class TestPerformance(BaseTestCase):
    """
    Assumes a project with key AWS already exists and has been configured and synced with AWS.

    N.B. Ensure that the sync intervals are high (i.e. no more than daily (1440 minutes)) and that any running sync has
    completed before performing any timed tests. Tests should not include waiting for any update from AWS.
    """

    project_key: str = "AWS"

    # def test_service_catalog(self):
    #     # page = self.navigator.login()
    #     # click create in top menu
    #     # select AWS project
    #     # select Service Catalog issue type
    #     #

    def test_navigator_login(self):
        self.navigator.login()

    # def test_ops_items_create_and_resolve(self):
    #     """create an ops item issue and resolve it"""
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
