from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_signup(name, email, password, expected_result):
    driver = webdriver.Chrome() 
    driver.get("https://example.com/signup") 
    
    
    name_input = driver.find_element(By.NAME, "name")
    email_input = driver.find_element(By.NAME, "email")
    password_input = driver.find_element(By.NAME, "password")
    submit_button = driver.find_element(By.ID, "signup-btn")  
    
    
    name_input.send_keys(name)
    email_input.send_keys(email)
    password_input.send_keys(password)
    submit_button.click()
    
    time.sleep(3)  

