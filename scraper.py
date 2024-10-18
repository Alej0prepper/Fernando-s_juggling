import logging
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up logging to print to the console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--window-size=1920x1080")  # Set window size

# Specify the path to the ChromeDriver executable
chrome_driver_path = '/usr/bin/chromedriver'  # Replace with the path to your ChromeDriver

# Set up the ChromeDriver service
service = Service(chrome_driver_path)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)
logging.info("Initialized WebDriver and ChromeDriver")

# Function to enter a siteswap string and click a button
def input_siteswap_and_click(siteswaps, input_selector, button_selector):
    try:
        # Open the website
        driver.get("https://www.jugglingedge.com/help/siteswapanimator.php")
        logging.info("Opened the website")

        for index, siteswap in enumerate(siteswaps):
            # Ensure the siteswap is a string
            if not isinstance(siteswap, str):
                siteswap = str(siteswap)

            # For subsequent siteswaps, wait for the user to press the Enter key
            if index > 0:
                input(f"Press Enter to input the next siteswap: {siteswap}")

            # Find the input element and enter the siteswap string
            input_element = driver.find_element(By.ID, input_selector)
            input_element.clear()
            input_element.send_keys(siteswap)
            logging.info(f"Entered siteswap string: {siteswap}")

            # Find the button element and click it
            button_element = driver.find_element(By.CSS_SELECTOR, button_selector)
            button_element.click()

            # Wait for a while to observe the result
            time.sleep(1)

        # After processing the last siteswap, wait for the user to press Enter before closing the WebDriver
        input("Press Enter to close the app")

    except Exception as e:
        logging.error(f"Error inputting siteswap and clicking button: {e}")
    finally:
        # Close the WebDriver
        driver.quit()
        logging.info("Closed the WebDriver")