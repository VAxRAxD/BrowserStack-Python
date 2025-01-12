import re, subprocess, urllib.parse, json
from playwright.sync_api import sync_playwright

def test_example(playwright):
    desired_cap={
        "capabilities": {
            "buildName": "browserstack-build-parallel",
            "sessionName": "Sample Playwright Test",
        },
        "environments": [
            {
                "os": "Windows",
                "os_version": "11",
                "name": "Test on Chrome latest on Windows 11",
                "browser": "chrome",
                "browser_version": "latest"
            },
            {
                "os": "OS X",
                "os_version": "Ventura",
                "name": "Test on Webkit latest on Ventura OS",
                "browser": "playwright-webkit",
                "browser_version": "latest"
            }
        ]
    }
    clientPlaywrightVersion = str(subprocess.getoutput('playwright --version')).strip().split(" ")[1]
    desired_cap['client.playwrightVersion'] = clientPlaywrightVersion
    cdpUrl = 'wss://cdp.browserstack.com/playwright?caps=' + urllib.parse.quote(json.dumps(desired_cap))
    browser = playwright.chromium.connect(cdpUrl)
    page = browser.new_page()
    page.goto("https://bstackdemo.com/")
    page.get_by_role("link", name="Sign In").click()
    page.locator("div").filter(has_text=re.compile(r"^Select Username$")).nth(2).click()
    page.get_by_text("demouser", exact=True).click()
    page.locator("div").filter(has_text=re.compile(r"^Select Password$")).nth(2).click()
    page.get_by_text("testingisfun99", exact=True).click()
    page.get_by_role("button", name="Log In").click()
    page.locator("[id=\"\\31 \"]").get_by_text("Add to cart").click()
    page.get_by_text("Checkout").click()
    page.get_by_label("First Name").click()
    page.get_by_label("First Name").fill("Varad")
    page.get_by_label("Last Name").click()
    page.get_by_label("Last Name").fill("Prabhu")
    page.get_by_label("Address").click()
    page.get_by_label("Address").fill("Dadar")
    page.get_by_label("State/Province").click()
    page.get_by_label("State/Province").fill("Maharashtra")
    page.get_by_label("Postal Code").click()
    page.get_by_label("Postal Code").fill("Dadar")
    page.get_by_role("button", name="Submit").click()
    confirmation_message = page.inner_text('#confirmation-message')
    try:
        assert confirmation_message == "Your Order has been successfully placed."
        page.evaluate("_ => {}", 'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Successfully Verified!"}}');
    except Exception as err:
        page.evaluate("_ => {}", 'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Test Failed!"}}');
        raise Exception
    page.close()
    
with sync_playwright() as playwright:
    test_example(playwright)