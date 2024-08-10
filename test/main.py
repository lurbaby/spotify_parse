# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# from webdriver_manager.firefox import GeckoDriverManager

# def setup_driver():
#     """Налаштування драйвера Selenium для Firefox"""
#     options = webdriver.FirefoxOptions()
#     # options.add_argument('--headless')  # Запуск в фоновому режимі
#     driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
#     return driver

# def fetch_page(driver, url):
#     """Функція для завантаження сторінки"""
#     driver.get(url)
#     # Зачекаємо, поки сторінка повністю завантажиться
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, 'btE2c3IKaOXZ4VNAb8WQ'))
#     )

# def find_elements_by_class_name(driver, class_name):
#     """Функція для пошуку елементів за назвою класу"""
#     try:
#         elements = driver.find_elements(By.CLASS_NAME, class_name)
#         return elements
#     except Exception as e:
#         print(f"Error finding elements: {e}")
#         return None

# def main():
#     url = 'https://open.spotify.com/playlist/2oHkKiDU77UwuDIb2LXzuW?si=1e972c2867354ad2&nd=1&dlsi=0a9c418dd70844da'  # Введіть URL для скрапінгу
#     driver = setup_driver()
#     fetch_page(driver, url)
    
#     class_name = 'btE2c3IKaOXZ4VNAb8WQ'
#     elements = find_elements_by_class_name(driver, class_name)
    
#     # Використовуйте знайдені елементи як вам потрібно
#     if elements:
#         for i, element in enumerate(elements):
#             print(f"Елемент {i+1}\n\n: {element}")
#             print()
#     else:
#         print("Елементи за назвою класу не знайдено")
    
#     driver.quit()

# if __name__ == "__main__":
#     main()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.firefox import GeckoDriverManager
import time

# def setup_driver():
#     """Налаштування драйвера Selenium для Firefox"""
#     options = webdriver.FirefoxOptions()
#     # options.add_argument('--headless')  # Запуск в фоновому режимі
#     driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
#     return driver

# def fetch_page(driver, url):
#     """Функція для завантаження сторінки"""
#     driver.get(url)

# def scroll_to_bottom(driver):
#     """Функція для прокрутки сторінки до самого низу"""
#     SCROLL_PAUSE_TIME = 2
#     last_height = driver.execute_script("return document.body.scrollHeight")

#     while True:
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(SCROLL_PAUSE_TIME)
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             break
#         last_height = new_height

# def find_elements_by_class_name(driver, class_name):
#     """Функція для пошуку елементів за назвою класу"""
#     try:
#         elements = driver.find_elements(By.CLASS_NAME, class_name)
#         return elements
#     except Exception as e:
#         print(f"Error finding elements: {e}")
#         return None

# def main():
#     url = 'https://open.spotify.com/playlist/2oHkKiDU77UwuDIb2LXzuW?si=1e972c2867354ad2&nd=1&dlsi=0a9c418dd70844da'  # Введіть URL для скрапінгу
#     driver = setup_driver()
    
#     # Прокручуємо сторінку до самого низу, щоб підвантажилися всі елементи
#     scroll_to_bottom(driver)
#     fetch_page(driver, url)
    

#     class_name = 'btE2c3IKaOXZ4VNAb8WQ'
#     elements = find_elements_by_class_name(driver, class_name)
    
#     # Використовуйте знайдені елементи як вам потрібно
#     if elements:
#         for i, element in enumerate(elements):
#             print(f"Елемент {i+1}: {element.text}")
#     else:
#         print("Елементи за назвою класу не знайдено")
    
#     driver.quit()

# if __name__ == "__main__":
#     main()






from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ініціалізація WebDriver (в даному випадку Chrome)
driver = webdriver.Chrome()
url = 'https://open.spotify.com/playlist/2oHkKiDU77UwuDIb2LXzuW?si=1e972c2867354ad2&nd=1&dlsi=0a9c418dd70844da'  # Введіть URL для скрапінгу

# driver = webdriver.Chrome()

driver.get(url)

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    try:
        WebDriverWait(driver, 10).until(
            lambda driver: driver.execute_script("return document.body.scrollHeight") > last_height
        )
    except:
        print("No new elements loaded after scrolling.")
        break

    # Оновлення останньої висоти прокрутки
    new_height = driver.execute_script("return document.body.scrollHeight")

    # Перевірка, чи з'явилися нові елементи
    if new_height == last_height:
        print("Reached the end of the page.")
        break  # Вихід з циклу, якщо нові елементи не з'явилися

    last_height = new_height
    time.sleep(2)  # Додавання затримки для надійності

# Отримання HTML-коду всієї сторінки
html = driver.page_source

with open("response.html", "w") as w:
    w.write(html)

# print(html)

# Закриття браузера
driver.quit()
