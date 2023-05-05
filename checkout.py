from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()

# Navigate to the inventory page
driver.get("https://www.saucedemo.com/inventory.html")

# Sort products from low price to high price
sort_dropdown = driver.find_element_by_css_selector(".product_sort_container")
sort_dropdown.click()
driver.find_element_by_css_selector('option[value="lohi"]').click()

# Add the lowest priced product to the cart
add_to_cart_button = driver.find_element_by_css_selector(".inventory_item:nth-child(1) .btn_inventory")
add_to_cart_button.click()

# Click on the cart
cart_button = driver.find_element_by_css_selector(".shopping_cart_container")
cart_button.click()

# Click on the checkout button
checkout_button = driver.find_element_by_css_selector(".checkout_button")
checkout_button.click()

# Enter user information
first_name_field = driver.find_element_by_id("first-name")
first_name_field.send_keys("John")
last_name_field = driver.find_element_by_id("last-name")
last_name_field.send_keys("Doe")
zip_code_field = driver.find_element_by_id("postal-code")
zip_code_field.send_keys("123")

# Click on the Continue button
continue_button = driver.find_element_by_css_selector(".cart_button")
continue_button.click()

# Verify that the total amount for the added item is $8.63
assert driver.find_element_by_css_selector(".summary_total_label").text == "Total: $8.63"

# Click on the Finish button
finish_button = driver.find_element_by_css_selector(".cart_button")
finish_button.click()

# Verify that the Thank You header is shown in the Checkout Complete page
assert driver.find_element_by_css_selector(".complete-header").text == "THANK YOU FOR YOUR ORDER"

