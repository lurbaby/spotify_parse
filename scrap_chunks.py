import asyncio
from playwright.async_api import async_playwright
from playwright.async_api import Page
from parse_chunks import song_count_spofify

# Rock
# url = "https://open.spotify.com/playlist/4FQOvPkvp1aG5iuSIf48ZB?si=b870032f1f094f90"

# Pospunk
# url = "https://open.spotify.com/playlist/2oHkKiDU77UwuDIb2LXzuW?si=1e972c2867354ad2&nd=1&dlsi=0a9c418dd70844da"

url = "https://open.spotify.com/playlist/2oHkKiDU77UwuDIb2LXzuW"

chunk_1_filename = "source/chunk_1_postpunk.html"
chunk_2_filename = "source/chunk_2_postpunk.html"

# Test my playlist
# url = "https://open.spotify.com/playlist/1JK8iAG2p3eZc6wH4oKWeO"

# chunk_1_filename = "source/chunk_1_tt.html"
# chunk_2_filename = "source/chunk_2_tt.html"



async def scroll_down(page: Page, scroll_count: int):
    for _ in range(scroll_count):
        await page.keyboard.press("ArrowDown")
        await asyncio.sleep(0.1)

async def main(chunks = 1):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        await page.goto(url)

        # Очікуємо завантаження основного контенту
        await page.wait_for_selector('div[class="contentSpacing"]', timeout=60000)
        # await asyncio.sleep(5)

        for i in range(chunks):

            await page.evaluate('''() => {
                const scripts = document.querySelectorAll('script');
                scripts.forEach(script => {
                    script.type = 'javascript/blocked';
                });
            }''')
            content = await page.content()
            # Записуємо HTML код у файл
            with open(f'{chunk_1_filename}', 'w', encoding='utf-8') as file:
                file.write(content)
            

            # Прокручуємо сторінку вниз для завантаження всього контенту
            previous_track_count = 0
            retry_count = 0
            
            while retry_count < 1:  # Намагаємося кілька разів, якщо контент перестає завантажуватись
                await scroll_down(page, 20)  # Скролимо сторінку вниз 100 разів
                # await asyncio.sleep(2)  # Чекаємо завантаження контенту
                
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
            with open(f'{chunk_2_filename}', 'w', encoding='utf-8') as file:
                file.write(content)
        
        await browser.close()

# asyncio.run(main( int(song_count_spofify / 50 ) ))
asyncio.run(main())
