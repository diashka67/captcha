from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def get_capcha(temp_dir):
    driver = webdriver.Chrome()
    driver.get('https://www.prepostseo.com/ru/image-to-text')
    
    file_inp = os.path.join(temp_dir, "result.png")

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
    element.send_keys(file_inp)
    time.sleep(2)

    element2 = driver.find_element(By.XPATH, '/html/body/main/section[1]/div[4]/div[3]/div[1]')
    element2.click()
    time.sleep(10)

    element3 = driver.find_element(By.XPATH, '//*[@id="result__text0"]').text
    driver.quit()
    return element3