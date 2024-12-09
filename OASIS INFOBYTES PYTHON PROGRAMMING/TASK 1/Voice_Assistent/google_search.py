from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def google_search_info(query):
    heading = ""
    description = ""
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        heading = driver.find_element(By.CSS_SELECTOR, "h3").text
        description = driver.find_element(By.CSS_SELECTOR, ".VwiC3b").text
        driver.quit()
    except:
        driver.quit()
    return heading, description

