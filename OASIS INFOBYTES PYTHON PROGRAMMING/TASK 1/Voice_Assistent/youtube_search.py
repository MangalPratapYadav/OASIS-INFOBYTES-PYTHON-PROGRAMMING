from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def youtube_search_and_play(query):
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.youtube.com")
        time.sleep(3)
        search_box = driver.find_element(By.NAME, "search_query")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="video-title"]').click()
        time.sleep(5)
        while True:
            try:
                driver.find_element(By.CLASS_NAME, "ytp-ad-skip-button").click()
                break
            except:
                time.sleep(1)
            if time.time() > 10:
                break
        while True:
            time.sleep(10)
    except:
        driver.quit()
