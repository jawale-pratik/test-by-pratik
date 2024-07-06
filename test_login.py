from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open Amazon.in login page
driver.get("https://www.amazon.in/ap/signin")

# Wait for the page to load
time.sleep(2)

# Find the email/phone number input box
username_box = driver.find_element(By.ID, "ap_email")

# Enter the username (email/phone number)
username_box.send_keys("your_email_or_phone")

# Click continue
continue_button = driver.find_element(By.ID, "continue")
continue_button.click()

# Wait for the next page to load
time.sleep(2)

# Find the password input box
password_box = driver.find_element(By.ID, "ap_password")

# Enter the password
password_box.send_keys("your_password")

# Click the login button
login_button = driver.find_element(By.ID, "signInSubmit")
login_button.click()

# Wait to observe the result (You may want to adjust the sleep time)
time.sleep(5)

# Close the browser
driver.quit()
