# import asyncio
# from playwright.async_api import async_playwright
# from playwright.async_api import Page
# from parse_chunks import final_links_arr

# data = []

# async def open_url(browser, url: None, urls):
#     pages = [i for i in range(len(final_links_arr))]
    
#     for i in range(len(urls)):
#         pages[i] = await browser.new_page()
#         await pages[i].goto(urls[i])

#     async def fetch_data(pages):
#         for i in range(len(pages)):
#             await pages[i].wait_for_selector('section[data-testid="track-page"]', timeout=60000)
#             await pages[i].wait_for_selector('span[data-testid="playcount"]', timeout=60000)

#             playcount = await pages[i].text_content('span[data-testid="playcount"]')
#             print(playcount)
#             await pages[i].close()
#             # content = page.content()
#         # data.append(content)
    
#     await asyncio.gather()

#     return await fetch_data(pages)

# #Fb61sprjhh75aOITDnsJ

# async def main(chunks = 1):

#     urls = None
#     true = False
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=true)
        
        
#         with open(f"{final_links_arr}", "r") as read_links:
#             urls = read_links.read().split('\n')[:-1]


#         # for url in urls:
#         # tasks = [open_url(browser, None, urls) ]
#         await open_url(browser, None, urls) 

        
#         # print()
        
#         # content = await page.content()

# asyncio.run(main())



import asyncio
from playwright.async_api import async_playwright
from parse_chunks import final_links_arr

skip_list = ["https://open.spotify.com/track/388my6QJ7CF9cxtp5fYxZX", "https://open.spotify.com/track/3CrqUzL4JeZRDtXOSFJs0t", "https://open.spotify.com/track/170XVDiX3YPeENm0qgZXC3"]


async def fetch_data(page, url, index):
    try:
        if not url in skip_list:            

            await asyncio.sleep(0.3)
            await page.goto(url, wait_until="domcontentloaded", timeout=60000)
            await page.wait_for_selector('section[data-testid="track-page"]', timeout=60000)
            await page.wait_for_selector('span[data-testid="playcount"]', timeout=60000)

            playcount = await page.text_content('span[data-testid="playcount"]')
            # dict[url] = playcount
            with open(r"playcount_result.txt", 'a') as write_res:
                write_res.write(f"{url} {playcount}\n")


    except Exception as e:
        print(f"Error fetching data from {url} [{index}]: {e}")
    
    finally:
        await page.close()

async def open_urls_in_parallel(browser, urls, max_concurrent_tabs=10):
    semaphore = asyncio.Semaphore(max_concurrent_tabs)
    
    async def fetch_with_semaphore(url, index):
        async with semaphore:
            page = await browser.new_page()
            await fetch_data(page, url, index)
    
    tasks = [fetch_with_semaphore(url, index + 1) for index, url in enumerate(urls)]
    await asyncio.gather(*tasks)

async def main(chunks=1):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        with open(f"{final_links_arr}", "r") as read_links:
            urls = read_links.read().split('\n')[:-1]

        await open_urls_in_parallel(browser, urls)

        await browser.close()

asyncio.run(main())
