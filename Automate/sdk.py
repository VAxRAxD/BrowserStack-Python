from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
import json

options = ChromeOptions()
options.set_capability('sessionName', 'BStack Sample Test')
driver = webdriver.Chrome(options=options)

try:
    driver.get('https://bstackdemo.com/')
    driver.implicitly_wait(10)
    driver.find_element(By.ID,'signin').click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#username input')))
    username = driver.find_element(By.CSS_SELECTOR, "#username input")
    username.send_keys("fav_user\n")
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password input')))
    password = driver.find_element(By.CSS_SELECTOR, "#password input")
    password.send_keys("testingisfun99\n")
    driver.find_element(By.ID,'login-btn').click()
    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="1"]/div[4]')))
    driver.find_element(By.XPATH,'//*[@id="1"]/div[4]').click()
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[2]/div[2]/div[3]/div[3]').click()
    WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,'firstNameInput')))
    driver.find_element(By.ID,'firstNameInput').send_keys('Varad')
    driver.find_element(By.ID,'lastNameInput').send_keys('Prabhu')
    driver.find_element(By.ID,'addressLine1Input').send_keys("Dadar")
    driver.find_element(By.ID,'provinceInput').send_keys("Maharashtra")
    driver.find_element(By.ID,'postCodeInput').send_keys('400028')
    driver.find_element(By.ID,'checkout-shipping-continue').click()
    if driver.find_element(By.ID,'confirmation-message').text=="Your Order has been successfully placed.":
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Successfully Verified!"}}')
    else:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Orders cannot be verified!"}}')
except Exception as err:
    message = "Exception: " + str(err.__class__) + str(err.msg)
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')
driver.quit()