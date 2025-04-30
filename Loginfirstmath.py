import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Maximize window
driver.maximize_window()

# Step 1: Open the website
driver.get("http://13.236.95.158/")
time.sleep(5)  # Wait for the page to load

# Step 2: Click the "Sign up" button
try:
    signup_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "landing-button"))
    )
    signup_button.click()
    print("✅ Clicked Sign Up")
except Exception as e:
    print("❌ Failed to click Sign Up:", e)

# Step 3: Wait for the page to load after clicking
time.sleep(3)

# Step 4: Click the "Sign in" link
try:
    signin_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
    )
    signin_link.click()
    print("✅ Clicked Sign In")
except Exception as e:
    print("❌ Failed to click Sign In:", e)

# Step 5: Wait for the sign-in form to load
time.sleep(5)

# Step 6: Fill in the email field using ID
try:
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    email_input.clear()  # Clear any existing text
    email_input.send_keys("ayushacarkey708@gmail.com")
    print("✅ Email entered successfully.")
except Exception as e:
    print("❌ Failed to enter email:", e)

# Optional wait to observe the result
time.sleep(5)

driver.find_element(By.ID, "password").send_keys("Test@123")
#Scroll to bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

driver.find_element(By.CLASS_NAME, "login-btn").click()
time.sleep(5)

# Optional: Close the browser
driver.quit()






