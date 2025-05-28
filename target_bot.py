import asyncio
import time
from playwright.async_api import async_playwright
from telegram_bot import send_telegram_message

class TargetBot:
    def __init__(self, sku_list, check_interval=30, max_quantity=1, heartbeat_hours=3):
        self.sku_list = sku_list
        self.check_interval = check_interval
        self.max_quantity = max_quantity
        self.heartbeat_hours = heartbeat_hours
        self.last_heartbeat = time.time()

    async def check_items(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            for sku in self.sku_list:
                url = f"https://www.target.com/p/-/{sku}"
                await page.goto(url)
                await page.wait_for_timeout(2000)

                try:
                    button = await page.query_selector("button[data-test='orderPickupButton']")
                    if button:
                        await send_telegram_message(f"🔥 Target restock detected! Try buying now:\n{url}")
                        for i in range(self.max_quantity):
                            await page.click("button[data-test='orderPickupButton']")
                            await page.wait_for_timeout(500)
                except:
                    pass  # Safe fail

            await browser.close()

    async def run(self):
        while True:
            await self.check_items()
            if time.time() - self.last_heartbeat > self.heartbeat_hours * 3600:
                await send_telegram_message("✅ Target bot check-in: still watching for Pokémon drops...")
                self.last_heartbeat = time.time()
            await asyncio.sleep(self.check_interval)
