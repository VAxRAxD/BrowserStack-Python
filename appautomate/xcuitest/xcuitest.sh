#!/bin/bash
APP_FILE_PATH="./BrowserStack-SampleApp.ipa"
TEST_FILE_PATH="./BrowserStack-SampleXCUITest.zip"

UPLOAD_RESPONSE=$(curl -u "$BROWSERSTACK_USERNAME:$BROWSERSTACK_ACCESS_KEY" \
-X POST "https://api-cloud.browserstack.com/app-automate/xcuitest/v2/app" \
-F "file=@$APP_FILE_PATH")

APP_URL=$(echo $UPLOAD_RESPONSE | sed -n 's/.*"app_url":"\([^"]*\)".*/\1/p')
if [ -z "$APP_URL" ]; then
  echo "Failed to upload the app."
  exit 1
fi
echo "App uploaded successfully: $APP_URL"

UPLOAD_RESPONSE=$(curl -u "$BROWSERSTACK_USERNAME:$BROWSERSTACK_ACCESS_KEY" \
-X POST "https://api-cloud.browserstack.com/app-automate/xcuitest/v2/test-suite" \
-F "file=@$TEST_FILE_PATH")

TEST_SUITE_URL=$(echo $UPLOAD_RESPONSE | sed -n 's/.*"test_suite_url":"\([^"]*\)".*/\1/p')
if [ -z "$TEST_SUITE_URL" ]; then
  echo "Failed to upload the test suite."
  exit 1
fi
echo "Test suite uploaded successfully: $TEST_SUITE_URL"

RUN_RESPONSE=$(curl -u "$BROWSERSTACK_USERNAME:$BROWSERSTACK_ACCESS_KEY" \
-X POST "https://api-cloud.browserstack.com/app-automate/xcuitest/v2/build" \
-d "{\"app\": \"$APP_URL\", \"testSuite\": \"$TEST_SUITE_URL\", \"devices\": [\"iPhone 11-13\"]}" \
-H "Content-Type: application/json")
echo "Test run response: $RUN_RESPONSE"