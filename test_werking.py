from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

email_or_phone = 'prachi._.sharma.01'

# Path to your WebDriver executable
# Example for ChromeDriver: r'C:\path\to\chromedriver.exe'
driver_path = 'C:\\Users\\user\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'


service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.instagram.com/accounts/password/reset/")

try:
    # It's better to wait for elements to be interactable
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "cppEmailOrUsername"))).send_keys(email_or_phone)

    # Construct a simpler, more stable XPath expression
    send_button_xpath = "//div[contains(@class, 'x1i10hfl') and contains(@class, 'xjqpnuy') and @role='button'][contains(text(), 'Send login link')]"
    
    # First, try to click the button normally
    try:
        send_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, send_button_xpath)))
        send_button.click()
    except Exception as click_exception:
        print("Standard click attempt failed:", click_exception)
        # As a fallback, use JavaScript to click the button
        send_button_js = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, send_button_xpath)))
        driver.execute_script("arguments[0].click();", send_button_js)

    time.sleep(5)
    
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()