from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from capcha import get_capcha
from photo import photo_bright
import os

# Получаем путь к папке, где лежит main.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_DIR = os.path.join(BASE_DIR, "captcha_temp")

# Создаём папку, если её нет
os.makedirs(TEMP_DIR, exist_ok=True)

driver = webdriver.Chrome()
driver.get('https://issaold.beltelecom.by/main.html')

# Скриншот капчи
screenshot_path = os.path.join(TEMP_DIR, "secpic4.png")
element1 = driver.find_element(By.XPATH, '//*[@id="capcher"]')
element1.screenshot(screenshot_path)

# Улучшаем картинку
photo_bright(TEMP_DIR)

# Распознаём капчу
captcha_text = get_capcha(TEMP_DIR)
print("Распознанная капча:", captcha_text)

# Вводим капчу
element2 = driver.find_element(By.XPATH, '//*[@id="cap_field"]')
element2.clear()
element2.send_keys(captcha_text)
time.sleep(1)

# Логин и пароль
element4 = driver.find_element(By.XPATH, '//*[@id="oper_user"]')
element4.send_keys('unkown5325')

element5 = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div[2]/div[3]/form/div/div[2]/input')
element5.send_keys('parol12345')

# Кнопка входа
element3 = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div[2]/div[3]/form/div/div[4]/input')
element3.click()

# Удаляем временный файл
result_path = os.path.join(TEMP_DIR, "result.png")
if os.path.exists(result_path):
    os.remove(result_path)

input("Нажми Enter, чтобы закрыть...")
driver.quit()