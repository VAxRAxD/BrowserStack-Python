import os, json
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from percy import percy_screenshot

load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME")
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY")
URL = os.environ.get("URL")

bstack_options = {
    "osVersion" : "11",
    "os" : "Windows",
    "browserName" : "Chrome",
    "browserVersion":"125.0",
    "buildName" : "VAxRAxD",
    "sessionName" : "Sample Percy Test",
    "userName": BROWSERSTACK_USERNAME,
    "accessKey": BROWSERSTACK_ACCESS_KEY,
}

bstack_options["source"] = "python:sample-main:v1.0"
options = ChromeOptions()
options.set_capability('bstack:options', bstack_options)
browser = webdriver.Remote(URL, options=options)
try:
    browser.get('https://stackoverflow.com/')
    percy_screenshot(browser, 'Homepage', enableLayout=True)
    browser.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Successfully Verified!"}}')
except Exception as err:
    message = "Exception: " + str(err.__class__) + str(err.msg)
    browser.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')
browser.quit()