import asyncio
from target_bot import TargetBot
from telegram_bot import send_telegram_message

async def main():
    await send_telegram_message("✅ Target bot check-in: still watching for Pokémon drops...")

    bot = TargetBot(
        item_ids=["94300072", "93954435", "93803457", "94300069",
            "94300067", "94300053", "94300073", "88897904",
            "94411686", "94300082"
        ],
        max_quantity=2,
        check_interval=15,
        heartbeat_hours=3
    )
    await bot.run()

if __name__ == "__main__":
    asyncio.run(main())

