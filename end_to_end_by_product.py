from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open Amazon.in
driver.get("https://www.amazon.in")

# Wait for the page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))

# Find the search box and enter the search keyword
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Sony TV")
search_box.send_keys(Keys.RETURN)

# Wait for search results to load and click on the first product
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot div.s-result-item")))
first_product = driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot div.s-result-item")[0]
first_product.find_element(By.CSS_SELECTOR, "h2 a").click()

# Wait for the product page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "add-to-cart-button")))

# Click on the 'Add to Cart' button
add_to_cart_button = driver.find_element(By.ID, "add-to-cart-button")
add_to_cart_button.click()

# Wait for the cart to update and proceed to checkout
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "hlb-ptc-btn-native")))
proceed_to_checkout_button = driver.find_element(By.ID, "hlb-ptc-btn-native")
proceed_to_checkout_button.click()

# Wait for the login page to load and fill in the login details
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ap_email")))
username_box = driver.find_element(By.ID, "ap_email")
username_box.send_keys("your_email_or_phone")

# Click continue
driver.find_element(By.ID, "continue").click()

# Wait for the password field to appear and fill in the password
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ap_password")))
password_box = driver.find_element(By.ID, "ap_password")
password_box.send_keys("your_password")

# Click the login button
driver.find_element(By.ID, "signInSubmit").click()

# Wait to observe the result (you can adjust the sleep time)
time.sleep(5)

# Close the browser
driver.quit()
