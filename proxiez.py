from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def create_driver_with_proxy(proxy):
    chrome_options = Options()
    chrome_options.add_argument(f'--proxy-server={proxy}')
    service = Service(executable_path=r'path_to_your_webdriver')
    driver = webdriver.Chrome(options=chrome_options, service=service)
    return driver

def read_proxies_from_file(file_path='proxies.txt'):
    with open(file_path, 'r') as file:
        proxies = [line.strip() for line in file.readlines()]
    return proxies

def main():
    proxies = read_proxies_from_file()
    for proxy in proxies:
        print(f"Using proxy: {proxy}")
        driver = create_driver_with_proxy(proxy)
        try:
            driver.get("https://www.instagram.com/accounts/password/reset/")
            # Add your logic here
            # Example: Fill the form
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "cppEmailOrUsername"))).send_keys('your_email_or_phone')
            # Implement the click on the "Send login link" button as needed
            # ...
            
            time.sleep(5)  # Adjust based on your needs

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            driver.quit()
        
        time.sleep(60)  # Wait for one minute before using the next proxy

if __name__ == "__main__":
    main()