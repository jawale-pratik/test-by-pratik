from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open Amazon.in
driver.get("https://www.amazon.in")

# Find the search box
search_box = driver.find_element(By.ID, "twotabsearchtextbox")

# Enter the search keyword and hit enter
search_box.send_keys("redmi mobiles")
search_box.send_keys(Keys.RETURN)s

# Wait for search results to load
time.sleep(3)

# Get the titles of the first few search results
results = driver.find_elements(By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal")

for index, result in enumerate(results[:10]):
    print(f"{index + 1}. {result.text}")

# Close the browser
driver.quit()

