from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from speedtest import get_internet_speed

download, upload = get_internet_speed()
promised_down = 150
promised_up = 150
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=options)

driver.get("https://x.com/home")
time.sleep(5)

if download < promised_down or upload < promised_up:
    tweet_box = driver.find_element(By.CSS_SELECTOR, ".public-DraftStyleDefault-block")
    tweet_box.send_keys(f"Hey provider, why is my internet speed {download} down/{upload} up when i pay for {promised_down} down/{promised_up} up ?")

    driver.find_element(By.CSS_SELECTOR, "button[data-testid='tweetButtonInline']").click()
