from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Replace 'your_email_or_phone' with the email or phone number you want to use
email_or_phone = 'prachi._.sharma.01'

# Path to your WebDriver executable
# Example for ChromeDriver: r'C:\path\to\chromedriver.exe'
driver_path = 'C:\\Users\\user\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'


# Initialize the WebDriver with the `Service` class
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

# Open the Instagram password reset page
driver.get("https://www.instagram.com/accounts/password/reset/")

# Wait for the page to load
time.sleep(5)

try:
    # The class name might have changed. If this doesn't work, check the current class name on the Instagram site.
    input_box_class = "_aaie._aaig._adrq._adrr._aaic._ag7n"  # This class name is subject to change
    input_box = driver.find_element(By.CLASS_NAME, input_box_class.replace(".", ""))
    
    # Input the email or phone number
    input_box.send_keys(email_or_phone)
    
    # Wait a bit for any dynamic page elements to update
    time.sleep(2)
    
    # Attempt to find and click the "Send Login Link" button
    # Note: This approach may need adjustment if the button's properties change
    send_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Send Login Link')]")
    send_button.click()
    
    # Wait to observe the action or for any follow-up
    time.sleep(5)
    
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the browser
    driver.quit()