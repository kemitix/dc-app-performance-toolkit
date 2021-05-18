from util.project_paths import JSM_YML
from .conftest import print_timing
from .navigator import Navigator


def aws_ping(driver):

    navigator = Navigator(driver, JSM_YML)
    expected_site_url = 'http://jira-loadb-11qi5gp1dvkil-717715101.us-east-1.elb.amazonaws.com:80'

    @print_timing("selenium_aws_ping")
    def tests():
        assert navigator is not None, "No navigator"
        assert navigator.driver is not None, "Navigator has no driver"
        assert navigator.site_url is not None, "Navigator has no url"
        assert navigator.site_user == 'admin', "Navigator has wrong user"
        assert navigator.site_password == 'c0nn3t0r', "Navigator has wrong password"
        assert navigator.site_url == expected_site_url, "Navigator has wrong url"
    tests()
