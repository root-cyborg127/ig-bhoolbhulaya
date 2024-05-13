from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Replace 'your_email_or_phone' with the email or phone number you want to use
email_or_phone = 'prachi._.sharma.01'

# Path to your WebDriver executable
# Example for ChromeDriver: 'C:/path/to/chromedriver.exe'
driver_path = 'C:\\Users\\user\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'

# Initialize the WebDriver (this example uses Chrome)
driver = webdriver.Chrome(executable_path=driver_path)

# Open the Instagram password reset page
driver.get("https://www.instagram.com/accounts/password/reset/")

# Wait for the page to load
time.sleep(5)

try:
    # Find the input box by its class name (note: this class name may change)
    input_box = driver.find_element(By.CLASS_NAME, "_aaie._aaig._adrq._adrr._aaic._ag7n")
    
    # Input the email or phone number
    input_box.send_keys(email_or_phone)
    
    # Wait a bit for any dynamic page elements to update
    time.sleep(2)
    
    # Find and click the "Send Login Link" button by its text (note: the approach may need to be adjusted if the structure changes)
    send_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Send Login Link')]")
    send_button.click()
    
    # Wait to observe the action or for any follow-up
    time.sleep(5)
    
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the browser
    driver.quit()