# import asyncio
# from playwright.async_api import async_playwright
# from playwright.async_api import Page
# import pyautogui
# import time

# # url = "https://open.spotify.com/playlist/2oHkKiDU77UwuDIb2LXzuW?si=1e972c2867354ad2"
# url = "https://open.spotify.com/playlist/1JK8iAG2p3eZc6wH4oKWeO" 


# chunk_1_filename = "source/chunk_1_postpunk.html"
# chunk_2_filename = "source/chunk_2_postpunk.html"

# # chunk_1_filename = "source/chunk_1_postpunk.html"
# # chunk_2_filename = "source/chunk_2_postpunk.html"
# timer = 5

# async def scroll_up_and_down(page: Page, scroll_count: int):
#     time.sleep(3)
#     for _ in range(scroll_count):
#         pyautogui.scroll(-200)  # Прокручуємо вниз
#         # time.sleep(2)
#         pyautogui.scroll(200)  # Прокручуємо вверх
#         # time.sleep(2)

# def set_min_zoom():

#     pyautogui.click(1170, 280)  # Клік на координатах, де знаходиться кнопка "Accept Cookies". Заміни координати на відповідні.

#     for _ in range(10):  # Натискаємо Ctrl+- кілька разів для зменшення масштабу
#         pyautogui.hotkey('ctrl', '-')
#         # time.sleep(0.5)
    
#     time.sleep(5)  # Чекаємо, щоб сторінка завантажилася
#     pyautogui.click(858, 1040)  # Клік на координатах, де знаходиться кнопка "Accept Cookies". Заміни координати на відповідні.

#     pyautogui.scroll(-100)

# async def main(chunks = 1):
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         context = await browser.new_context(viewport={"width": 1920, "height": 1080})
#         page = await context.new_page()

#         await page.goto(url)


#         # Зменшуємо масштаб сторінки до мінімального
#         set_min_zoom()
    
#         # Очікуємо завантаження основного контенту
#         await page.wait_for_selector('div[class="contentSpacing"]', timeout=60000)
#         await asyncio.sleep(timer)

#         await page.evaluate('''() => {
#             const scripts = document.querySelectorAll('script');
#             scripts.forEach(script => {
#                 script.type = 'javascript/blocked';
#             });
#         }''')
        

#         await scroll_up_and_down(page, 3)  # Скролимо сторінку вверх-вниз 10 разів

#         await asyncio.sleep(2)  # Чекаємо завантаження контенту

#         content = await page.content()
        
#         # Записуємо HTML код у файл
#         with open(f'{chunk_2_filename}', 'w', encoding='utf-8') as file:
#             file.write(content)
        
#         await browser.close()

# asyncio.run(main())


import asyncio
from playwright.async_api import async_playwright
from playwright.async_api import Page
import pyautogui
import time

# URL плейлиста на Spotify
# url = "https://open.spotify.com/playlist/1JK8iAG2p3eZc6wH4oKWeO"
url = "https://open.spotify.com/playlist/5Rrf7mqN8uus2AaQQQNdc1"


# Імена файлів для збереження HTML
chunk_2_filename = "source/chunk_2_postpunk.html"
timer = 5
scroll_count = 3

async def scroll_up_and_down(page: Page, scroll_count: int):
    time.sleep(3)
    all_content = []  # Список для збереження всіх частин HTML
    content = await page.content()
    all_content.append(content)


    for _ in range(scroll_count):
        # Прокручуємо вниз
        pyautogui.scroll(-20)
        # Отримуємо HTML-контент після прокручування вниз
        content = await page.content()
        all_content.append(content)
        await asyncio.sleep(5)

    # Повертаємо зібраний контент
    return all_content

def set_min_zoom():
    # Клік на кнопку "Accept Cookies"
    pyautogui.click(1170, 280)

    # Зменшуємо масштаб сторінки
    for _ in range(10):  # Натискаємо Ctrl+- кілька разів для зменшення масштабу
        pyautogui.hotkey('ctrl', '-')

    time.sleep(5)  # Чекаємо, щоб сторінка завантажилася

    # Клік на координатах іншої кнопки (можливо, знову "Accept Cookies")
    pyautogui.click(858, 1040)

    # Невеликий скрол після зменшення масштабу
    pyautogui.scroll(-100)

async def main(chunks=1):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={"width": 1920, "height": 1080})
        page = await context.new_page()

        await page.goto(url)

        # Зменшуємо масштаб сторінки до мінімального та натискаємо кнопку "Accept Cookies"
        set_min_zoom()

        # Очікуємо завантаження основного контенту
        await page.wait_for_selector('div[class="contentSpacing"]', timeout=60000)
        await asyncio.sleep(timer)

        await page.evaluate('''() => {
            const scripts = document.querySelectorAll('script');
            scripts.forEach(script => {
                script.type = 'javascript/blocked';
            });
        }''')

        # Прокручуємо сторінку вверх-вниз кілька разів і збираємо всі частини HTML
        all_content = await scroll_up_and_down(page, scroll_count)

        # Записуємо об'єднаний HTML-контент у файл
        with open(chunk_2_filename, 'w', encoding='utf-8') as file:
            file.write("\n".join(all_content))

        await browser.close()

asyncio.run(main())
