from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from dotenv import load_dotenv
import os, json, time
from browserstack.local import Local

load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME")
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY")
URL = os.environ.get("URL")

bs_local = Local()
bs_local_args = { "key": BROWSERSTACK_ACCESS_KEY }
bs_local.start(**bs_local_args)

bstack_options = {
    "os" : "Windows",
    "osVersion" : "10",
    "browserName" : "Chrome",
    "buildName" : "VAxRAxD",
    "sessionName" : "Sample Browser Local Test",
    "userName": BROWSERSTACK_USERNAME,
    "accessKey": BROWSERSTACK_ACCESS_KEY,
    "local": "true"
}

bstack_options["source"] = "python:sample-main:v1.0"
options = ChromeOptions()
options.set_capability('bstack:options', bstack_options)

driver=webdriver.Remote(URL, options=options)
try:
    driver.get('http://127.0.0.1:5000/')
    time.sleep(15)
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Successfully Verified!"}}')
except Exception as err:
    message = "Exception: " + str(err.__class__) + str(err.msg)
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')
bs_local.stop()
driver.quit()