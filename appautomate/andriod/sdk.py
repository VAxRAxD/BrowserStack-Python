import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

bstack_options = {
    "buildName" : "VAxRAxD",
    "sessionName" : "Sample Android SDK Test",
}
options = UiAutomator2Options().set_capability('bstack:options', bstack_options)

driver = webdriver.Remote(options=options)
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
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Product purchase successfull!!"}}')
except:
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Failed"}}')    
driver.quit()