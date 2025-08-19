from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_internet_speed(timeout=45):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://www.speedtest.net/")
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "a.js-start-test.test-mode-multi").click()
        time.sleep(timeout)
        results = driver.find_elements(By.CSS_SELECTOR, '.result-data span')
        speeds = [float(r.text.split()[0]) for r in results if r.text.strip()]
        driver.quit()
        return speeds
    except:
        get_internet_speed()


