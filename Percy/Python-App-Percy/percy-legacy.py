import os,time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from percy import percy_screenshot
from dotenv import load_dotenv

load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME")
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY")
URL = os.environ.get("URL")

options = UiAutomator2Options().load_capabilities({
    "platformName" : "android",
    "platformVersion" : "9.0",
    "deviceName" : "Google Pixel 3",
    "app" : "bs://85e577c7635c44fcb39b3c3985a6fd6d72139651",
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
    filter=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "filter-btn")))
    filter.click()
    phone=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Samsung\")")))
    phone.click()
    price=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"High to Low\")")))
    price.click()
    driver.press_keycode(4)
    cart=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "add-to-cart-12")))
    cart.click()
    cart_button=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"\")")))
    cart_button.click()
    chckout=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"CHECKOUT\")")))
    chckout.click()
    usrname=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "username-input")))
    usrname.click()
    usrval=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"demouser\")")))
    usrval.click()
    passwd=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "password-input")))
    passwd.click()
    passval=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"testingisfun99\")")))
    passval.click()
    login=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "login-btn")))
    login.click()
    usrname=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "firstNameInput"))).send_keys("Varad")
    lstname=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "lastNameInput"))).send_keys("Prabhu")
    usrname=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "addressInput"))).send_keys("Mumbai")
    usrname=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "stateInput"))).send_keys("Maharashtra")
    postal=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "postalCodeInput"))).send_keys("400028")
    shop=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "submit-btn")))
    shop .click()
    time.sleep(5)
    percy_screenshot(driver, 'Mobile Purchased')
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Product purchase successfull!!"}}')
except:
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Failed"}}')    
driver.quit()