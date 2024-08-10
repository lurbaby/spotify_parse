# import requests

# from bs4 import BeautifulSoup

# response = requests.get("https://open.spotify.com/playlist/2oHkKiDU77UwuDIb2LXzuW?si=1e972c2867354ad2&nd=1&dlsi=0a9c418dd70844da")
# print(response.text)
# # soup = BeautifulSoup(response, "lxml")


# ==========================================================================================================================================

# from selenium import webdriver

# # Ініціалізація WebDriver (в даному випадку Chrome)
# driver = webdriver.Chrome()

# # Завантаження веб-сторінки за вказаною URL-адресою
# driver.get("https://open.spotify.com/playlist/2oHkKiDU77UwuDIb2LXzuW?si=1e972c2867354ad2&nd=1&dlsi=0a9c418dd70844da")


# # Отримання HTML-коду всієї сторінки
# html = driver.page_source

# with open("response.html", "w") as w:
#     w.write(html)

# # print(html)

# # Закриття браузера
# driver.quit()






# ===========================================================================================================================================================


from time import sleep
from selenium import webdriver

# Ініціалізація WebDriver (в даному випадку Chrome)
driver = webdriver.Chrome()

# Встановлення неявного очікування (10 секунд)
driver.get("https://open.spotify.com/playlist/2oHkKiDU77UwuDIb2LXzuW?si=1e972c2867354ad2&nd=1&dlsi=0a9c418dd70844da")


driver.implicitly_wait(2000000000)
sleep(10)

# Отримання HTML-коду всієї сторінки
html = driver.page_source
with open("response.html", "w") as w:
    w.write(html)


# Закриття браузера
driver.quit()
