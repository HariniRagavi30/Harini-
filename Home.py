from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://cinimini.netlify.app/")
driver.maximize_window()
time.sleep(2)

login_button=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='login-btn']"))

)
login_button.click()
print("login p button clicked successfully")
time.sleep(2)

driver.get(" https://cinimini.netlify.app/loginpage/signup")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="username"]').send_keys("Harini")    
driver.find_element(By.XPATH,'//*[@id="email"]').send_keys("harini01@gmail.com")
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("Harini@2006")



signup_button=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="submit-btn"]'))

)
signup_button.click()
print("signup p button clicked successfully")
time.sleep(3)


driver.find_element(By.XPATH, '//*[@id="submit-btn"]').click()

print("signup p button clicked successfully")
time.sleep(5)


driver.find_element(By.XPATH,'//*[@id="submit-btn"]').click()


#search one movie 

Movie_name = "Home Alone"  
search_box = driver.find_element(By.XPATH, '//*[@id="search-bar"]')
search_box.send_keys("Home alone")
search_box.send_keys(Keys.RETURN)

time.sleep(3)

#click one movie 

first_movie = driver.find_element(By.XPATH,'//*[@id="movies-container"]/div[1]/img' )
first_movie.click()

time.sleep(3)
#Watch trailer

Watch_Trailer=driver.find_element(By.XPATH,'//*[@id="Trailer"]')
Watch_Trailer.click()
time.sleep(2)
#Add to wishlist
Add_to_Wishlist=driver.find_element(By.XPATH,'//*[@id="add-to-wishlist-btn"]')
Add_to_Wishlist.click()
time.sleep(2)


# Click on the first search result
first_result = driver.find_element(By.XPATH, "(//li[@class='ipc-metadata-list-summary-item']//a)[1]")
first_result.click()

# Wait for the movie details page to load
time.sleep(3)

# Extract movie details
movie_title = driver.find_element(By.XPATH, "//h1").text
movie_rating = driver.find_element(By.XPATH, "//span[contains(@class, 'sc-bde20123-1')]").text
movie_summary = driver.find_element(By.XPATH, "//span[@data-testid='plot-xl']").text

# Print the extracted details
print("Movie Title:", movie_title)
print("IMDb Rating:", movie_rating)
print("Summary:", movie_summary)

# Close the browser
driver.quit()