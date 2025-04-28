import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome using the correct Service object
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Maximize window
driver.maximize_window()

# Open the website
driver.get("http://13.236.95.158/")
time.sleep(5)


# Click the "Sign up" link
driver.find_element(By.CLASS_NAME, "landing-button").click()

# Wait a few seconds to see the result after clicking
time.sleep(5)

#Scroll to bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


#Wait after scrolling
time.sleep(2)

#Click the "Sign up" link using link text
driver.find_element(By.LINK_TEXT, "Sign up").click()

#Wait to observe the result
time.sleep(3)


# Step 5: Fill out the sign-up form
driver.find_element(By.ID, "full_name").send_keys("Ayusha Karki")
driver.find_element(By.ID, "email").send_keys("anujkarki005@gmail.com")
driver.find_element(By.ID, "password").send_keys("Test@123")
driver.find_element(By.ID, "password_confirmation").send_keys("Test@123")
time.sleep(3)
#Scroll to bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)



# Click the "Next Button" link
driver.find_element(By.CLASS_NAME, "next-btn").click()

time.sleep(10)



#Close the browser
driver.quit()

