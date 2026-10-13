from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from capcha import get_capcha
from photo import photo_bright
import os


driver = webdriver.Chrome()
driver.get('https://issaold.beltelecom.by/main.html')

element1 = driver.find_element(By.XPATH, '//*[@id="capcher"]')
element1.screenshot('captcha_temp/secpic4.png')
# element1.screenshot('captcha_temp/image.png')

photo_bright()

element2 = driver.find_element(By.XPATH, '//*[@id="cap_field"]')
element2.clear()
element2.send_keys(get_capcha())
time.sleep(2)

element4 = driver.find_element(By.XPATH, '//*[@id="oper_user"]')
element4.send_keys('unkown5325')

element5 = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div[2]/div[3]/form/div/div[2]/input')
element5.send_keys('parol12345')

element3 = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div[2]/div[3]/form/div/div[4]/input')
element3.click()

os.remove('captcha_temp/result.png')

input()