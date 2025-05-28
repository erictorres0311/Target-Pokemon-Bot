import asyncio
import time
from playwright.async_api import async_playwright
from telegram_bot import send_telegram_message

class TargetBot:
    def __init__(self, item_ids, check_interval=60, heartbeat_hours=3):
        self.item_ids = item_ids
        self.check_interval = check_interval
        self.heartbeat_hours = heartbeat_hours
        self.last_heartbeat = time.time()

    async def fetch_product_json(self, page, item_id):
        url = f"https://www.target.com/p/-/{item_id}"
        await page.goto(url, timeout=60000, wait_until='domcontentloaded')
        content = await page.content()
        if 'Product not available' in content or 'product not available' in content.lower():
            return None
        return url  # Assume available if page renders without product error

    async def check_items(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            for item_id in self.item_ids:
                try:
                    product_url = await self.fetch_product_json(page, item_id)
                    if product_url:
                        await send_telegram_message(f"🔥 Target restock detected! Try buying now:\n{product_url}")
                        print(f"[{item_id}] Restock detected: {product_url}")
                    else:
                        print(f"[{item_id}] Not in stock.")
                except Exception as e:
                    print(f"[{item_id}] Error: {e}")

            await browser.close()

    async def run(self):
        while True:
            await self.check_items()

            # Heartbeat message
            if time.time() - self.last_heartbeat > self.heartbeat_hours * 3600:
                await send_telegram_message("✅ Target bot check-in: still watching for Pokémon drops...")
                self.last_heartbeat = time.time()

            await asyncio.sleep(self.check_interval)
