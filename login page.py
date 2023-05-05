from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to the Demo Login Page
driver.get("https://www.saucedemo.com/")

# Fill in the account information for the StandardUser account
username_field = driver.find_element_by_id("user-name")
username_field.send_keys("standard_user")
password_field = driver.find_element_by_id("password")
password_field.send_keys("secret_sauce")

# Click the Login button
login_button = driver.find_element_by_id("login-button")
login_button.click()

# Verify that we have been redirected to the Demo Main Page
assert driver.current_url == "https://www.saucedemo.com/inventory.html"

# Verify that the App Logo exists
assert driver.find_element_by_class_name("app_logo")

# Close the browser window
driver.quit()
