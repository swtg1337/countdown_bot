import os
import asyncio
from datetime import date

from aiogram import Bot

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

TARGET_DATE = date(2025, 5, 27)

def get_day_word(n):
    if 10 <= n % 100 <= 20:
        return "дней"
    elif n % 10 == 1:
        return "день"
    elif 2 <= n % 10 <= 4:
        return "дня"
    else:
        return "дней"

def load_facts():
    facts = {}
    with open("facts_per_day.txt", "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(" ", 1)
            if len(parts) == 2:
                try:
                    days_left = int(parts[0])
                    fact = parts[1].strip()
                    facts[days_left] = fact
                except ValueError:
                    continue
    return facts

async def send_message():
    today = date.today()
    days_left = (TARGET_DATE - today).days

    day_word = get_day_word(days_left)

    facts = load_facts()

    if days_left > 0:
        fact_message = facts.get(days_left, "Серега лучший в мире.")
        message = f"До выхода Султана на свободу осталось {days_left} {day_word}! 🕊️\n\n{fact_message}"
    elif days_left == 0:
        message = "Сегодня день выхода Султана на свободу! 🎉"
    else:
        message = "Султан уже на свободе! 🚀"

    bot = Bot(token=TOKEN)
    await bot.send_message(CHAT_ID, message)
    await bot.session.close()

if __name__ == "__main__":
    asyncio.run(send_message())
