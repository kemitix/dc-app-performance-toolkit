# run this from the local command line
#
# e.g.:
# pytest run-test-in-local-chrome-driver.py

from selenium_ui.jsm import modules_agents
from selenium_ui.jsm_ui_agents import test_0_selenium_agent_a_login,test_1_selenium_aws_opsitems, test_2_selenium_agent_z_logout
from selenium_ui.conftest import Dataset
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

jsm_datasets = Dataset().jsm_dataset()

test_0_selenium_agent_a_login(driver, jsm_datasets, [])

test_1_selenium_aws_opsitems(driver, jsm_datasets, [])

test_2_selenium_agent_z_logout(driver, jsm_datasets, [])
