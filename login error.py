from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()

# Navigate to the Demo Login Page
driver.get("https://www.saucedemo.com/")

# Fill in the account information for the LockedOutUser account
username_field = driver.find_element_by_id("user-name")
username_field.send_keys("locked_out_user")
password_field = driver.find_element_by_id("password")
password_field.send_keys("secret_sauce")

# Click the Login button
login_button = driver.find_element_by_id("login-button")
login_button.click()

# Verify that the error message contains the text "Sorry, this user has been banned."
assert "Sorry, this user has been banned." in driver.page_source

# Close the browser window
driver.quit()
