import asyncio
from target_bot import TargetBot
from telegram_bot import send_telegram_message

async def main():
    await send_telegram_message("✅ Target bot check-in: still watching for Pokémon drops...")

    bot = TargetBot(
        sku_list=[  # ← CORRECT
            "94300072",  # Prismatic Evolutions Super Premium Collection
            "89462588",  # ETB Scarlet & Violet Base
            "87933082",  # ETB Paldea Evolved
            "89148990",  # ETB Obsidian Flames
            "89462584",  # ETB 151
            "89149002",  # ETB Paradox Rift
            "89462586",  # ETB Temporal Forces
            "89462592",  # ETB Twilight Masquerade
        ],
        check_interval=15,
        heartbeat_hours=3
    )
    await bot.run()

if __name__ == "__main__":
    asyncio.run(main())
