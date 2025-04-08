from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()  # Change to Edge() or Firefox() if needed
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")  # Replace with actual login page URL


time.sleep(2)  # Wait for the page to load

# Function to test login
def test_login(email, password):
    email_field = driver.find_element(By.ID, "username")  # Locate email field
    password_field = driver.find_element(By.ID, "password")  # Locate password field
    login_button = driver.find_element(By.ID, "login-btn")  # Locate login button
    
    email_field.clear()
    password_field.clear()

    email_field.send_keys(email)
    password_field.send_keys(password)
    login_button.click()
  
    time.sleep(2)  # Wait for response
 
#  Positive Test Cases
test_login("validuser@example.com", "ValidPass123")


#  Negative Test Cases
test_login("invalidemail.com", "ValidPass123")  # Missing "@"
test_login("user@", "ValidPass123")  # Missing domain
test_login("", "ValidPass123")  # Blank email
test_login("validuser@example.com", "")  # Blank password
test_login("validuser@example.com", "WrongPass123")  # Incorrect password

# Close the browser
driver.quit()














