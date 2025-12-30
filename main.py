from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import random

def check_stock():
    options = webdriver.ChromeOptions()
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    url = "https://shop.lululemon.com/p/womens-outerwear/Scuba-Oversized-Funnel-Neck-Long-MD/_/prod11690117?color=73482&sz=XS/S"
    try:
        while True:
            print("Searching...")
            driver.get(url)
            time.sleep(5)

            try:
                wait = WebDriverWait(driver, 20)
                print("Wait for page to load. ")
                container = driver.find_element(By.ID, "purchase-methods")
                all_buttons = container.find_elements(By. TAG_NAME, "button")

                found_actionable_button = False
                for btn in all_buttons:
                    text = btn.text.lower()
                    if "add to bag" in text:
                        print("Item of size s is available")
                        found_actionable_button = True
                        # send message to telegram
                        break
                    elif "sold out" in text or "notify me" in text:
                        print(f"[{time.strftime('%H:%M:%S')}] Confirmed: Button says '{btn.text}'. ")
                        found_actionable_button = True
                        break
                if not found_actionable_button:
                    print("Found the section, but couldn't find a Stock or Sold Out button yet. ")

                
            except Exception as e: #only runs if whole purch session is missing
                print("Page hasn't loaded the purchase section yet")

            wait_time = random.randint(300, 600)
            print(f"Refreshing in {wait_time // 60} minutes ... ")
            time.sleep(wait_time)
    finally:
        driver.quit()

check_stock()



