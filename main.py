from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import requests
import random
import os
from dotenv import load_dotenv

load_dotenv()

def send_telegram(message):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"

    try:
        requests.get(url)
    except Exception as e:
        print(f"Failed to send Telegram: {e}")

def check_stock():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new") # Runs Chrome in the background
    options.add_argument("--window-size=1920,1080") # Helps render the page correctly
    options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
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
                        msg = f"Lululemon: Your item is in stock! {url}"
                        send_telegram(msg)
                        print("Notification sent to Telegram")
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



