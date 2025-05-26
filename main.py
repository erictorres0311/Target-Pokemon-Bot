from target_bot import TargetBot
import time

if __name__ == "__main__":
    bot = TargetBot()
    bot.run(check_interval=15, heartbeat_interval_hours=3)