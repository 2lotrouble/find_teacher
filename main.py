import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from playsound import playsound

# Установка пути к драйверу для браузера Яндекс
driver_path = '/path/to/your/driver'
driver = webdriver.Chrome(driver_path)

# URL страницы с учителями
url = 'https://example.com/teachers'

# Имя учителя, которое мы ищем
target_name = 'John Smith'

while True:
    driver.get(url)
    try:
        # Проверяем наличие элемента с нужным именем
        element_present = EC.presence_of_element_located((By.XPATH, f"//div[@class='teacher-name' and text()='{target_name}']"))
        WebDriverWait(driver, 10).until(element_present)
        # Если имя найдено, воспроизводим звуковое уведомление
        playsound('/path/to/your/sound/file.mp3')
    except:
        pass
    # Ждем 10 секунд перед следующей проверкой
    time.sleep(10)

# Закрываем браузер
driver.quit()
