import os,time
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME")
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY")
URL = os.environ.get("URL") 

options = XCUITestOptions().load_capabilities({
    "platformName" : "ios",
    "platformVersion" : "15",
    "deviceName" : "iPhone 13",
    "app" : "bs://03193f5cb399d54556143b06989d98692a1314ec",
    'bstack:options' : {
        "projectName" : "Andriod App Automate project",
        "buildName" : "browserstack-build-12",
        "sessionName" : "BStack app_auto_test",
        "userName" : BROWSERSTACK_USERNAME,
        "accessKey" : BROWSERSTACK_ACCESS_KEY,
    }
})

driver = webdriver.Remote(URL, options=options)
try:
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Button"))).click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Input"))).click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Input"))).send_keys("Varad")
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Return"))).click()
    text=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Output"))).text
    time.sleep(5)
    if text=="Varad":
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Text verified!"}}')
    else:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Text not verified!"}}')
except:
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Failed"}}')    
driver.quit()