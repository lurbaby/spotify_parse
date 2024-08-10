# # url = "https://open.spotify.com/track/6AGTTs3G3mFSyeDknuNp02"
url = "https://open.spotify.com/playlist/2oHkKiDU77UwuDIb2LXzuW?si=1e972c2867354ad2&nd=1&dlsi=0a9c418dd70844da"

# import asyncio
# from playwright.async_api import async_playwright

# async def main():
#     async with async_playwright() as p:
#         # Вибираємо браузер (може бути 'chromium', 'firefox', або 'webkit')
#         browser = await p.chromium.launch(headless=False)  # headless=False для відладки
#         page = await browser.new_page()
        
#         # Відкриваємо сторінку
#         await page.goto(url)
        
#         # Очікуємо завантаження динамічного контенту
#         # await page.wait_for_selector('section[data-testid="track-page"]')
        
#         await page.wait_for_selector('div[class="contentSpacing"]')
        
        

#         # Скролимо сторінку вниз для завантаження динамічного контенту
#         last_height = await page.evaluate("document.body.scrollHeight")
#         while True:
#             # Скролимо вниз
#             await page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
            
#             # Чекаємо завантаження контенту
#             await asyncio.sleep(3)
            
#             # Отримуємо нову висоту сторінки
#             new_height = await page.evaluate("document.body.scrollHeight")
            
#             # Перевіряємо, чи не досягли кінця сторінки
#             if new_height == last_height:
#                 break
            
#             last_height = new_height
        
#         # await page.evaluate('''() => {
#         #     const scripts = document.querySelectorAll('script');
#         #     scripts.forEach(script => {
#         #         script.type = 'javascript/blocked';
#         #     });
#         # }''')


#         # Забираємо весь HTML код зі сторінки
#         content = await page.content()


        
#         with open(r"response_playlist.html", "w") as write:
#            write.write(content)

#         # Виводимо HTML код
#         print(200)
        
#         # Закриваємо браузер
#         await browser.close()

# # Запускаємо головну функцію
# asyncio.run(main())





# import asyncio
# from playwright.async_api import async_playwright

# async def main():
#     async with async_playwright() as p:
#         # Вибираємо браузер (може бути 'chromium', 'firefox', або 'webkit')
#         browser = await p.chromium.launch(headless=False)  # headless=False для відладки
#         page = await browser.new_page()
        
#         # Відкриваємо сторінку
#         await page.goto(url)
        
#         # Очікуємо завантаження першого блоку контенту
#         await page.wait_for_selector('div[class="contentSpacing"]')
        
#         # Функція для скролу сторінки вниз
#         async def scroll_page():
#             last_height = await page.evaluate("document.body.scrollHeight")
#             while True:
#                 await page.evaluate("window.scrollBy(0, window.innerHeight);")
#                 await asyncio.sleep(2)  # Чекаємо 2 секунди після кожного скролу
#                 new_height = await page.evaluate("document.body.scrollHeight")
                
#                 # Перевіряємо наявність нових елементів після скролу
#                 new_tracks = page.locator('div[class="contentSpacing"]')
#                 if await new_tracks.count() > 0:
#                     await asyncio.sleep(2)  # Чекаємо додатковий час для завантаження нових елементів

#                 if new_height == last_height:
#                     break
#                 last_height = new_height
        
#         # Виконуємо скрол сторінки вниз
#         await scroll_page()
        
#         # Відключаємо виконання скриптів
#         await page.evaluate('''() => {
#             const scripts = document.querySelectorAll('script');
#             scripts.forEach(script => {
#                 script.type = 'javascript/blocked';
#             });
#         }''')

#         # Забираємо весь HTML код зі сторінки
#         content = await page.content()
        
#         with open(r"response_playlist.html", "w") as write:
#             write.write(content)

#         # Виводимо HTML код
#         print("HTML контент збережено")
        
#         # Закриваємо браузер
#         await browser.close()

# # Запускаємо головну функцію
# url = "https://open.spotify.com/playlist/2oHkKiDU77UwuDIb2LXzuW?si=1e972c2867354ad2&nd=1&dlsi=0a9c418dd70844da"
# asyncio.run(main())

import asyncio
from playwright.async_api import async_playwright
from playwright.async_api import Page

async def scroll_down(page: Page, scroll_count: int):
    for _ in range(scroll_count):
        await page.keyboard.press("ArrowDown")
        await asyncio.sleep(1.5)

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        # url = 'URL_ВАШОЇ_СТОРІНКИ'  # Заміни на потрібний URL
        url2 = "https://open.spotify.com/playlist/4FQOvPkvp1aG5iuSIf48ZB?si=b870032f1f094f90"
        await page.goto(url2)
        
        # Очікуємо завантаження основного контенту
        await page.wait_for_selector('div[class="contentSpacing"]', timeout=60000)
        await asyncio.sleep(5)

        # Прокручуємо сторінку вниз для завантаження всього контенту
        previous_track_count = 0
        retry_count = 0
        
        while retry_count < 1:  # Намагаємося кілька разів, якщо контент перестає завантажуватись
            await scroll_down(page, 20)  # Скролимо сторінку вниз 100 разів
            await asyncio.sleep(2)  # Чекаємо завантаження контенту
            
            # Перевіряємо кількість завантажених треків
            current_track_count = await page.evaluate('''() => {
                return document.querySelectorAll('div[data-testid="tracklist-row"]').length;
            }''')
            
            if current_track_count == previous_track_count:
                retry_count += 1  # Збільшуємо лічильник спроб
            else:
                retry_count = 0  # Скидаємо лічильник спроб, якщо з'явилися нові елементи
                previous_track_count = current_track_count
        
        # Відключаємо всі скрипти на сторінці
        await page.evaluate('''() => {
            const scripts = document.querySelectorAll('script');
            scripts.forEach(script => {
                script.type = 'javascript/blocked';
            });
        }''')

        content = await page.content()
        
        # Записуємо HTML код у файл
        with open('page_content2.html', 'w', encoding='utf-8') as file:
            file.write(content)
        
        await browser.close()

asyncio.run(main())
