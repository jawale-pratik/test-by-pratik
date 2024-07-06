from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open Amazon.in
driver.get("https://www.amazon.in")

# Wait for the page to load
time.sleep(3)

# Find the search box
search_box = driver.find_element(By.ID, "twotabsearchtextbox")

# Enter the search keyword
search_box.send_keys("mi tv")
search_box.send_keys(Keys.RETURN)

# Wait for search results to load
time.sleep(3)

# Click on the first product
first_product = driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot div.s-result-item")[0]
first_product.find_element(By.CSS_SELECTOR, "h2 a").click()

# Wait for the product page to load
time.sleep(3)

# Click on the 'Add to Cart' button
add_to_cart_button = driver.find_element(By.ID, "add-to-cart-button")
add_to_cart_button.click()

# Wait for the cart to update
time.sleep(3)

# Close the browser
driver.quit()
