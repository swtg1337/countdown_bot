import os
import asyncio
from datetime import date
from aiogram import Bot, Dispatcher

# Берем токен и chat_id из переменных окружения (GitHub Actions будет их хранить)
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Дата, до которой считаем дни (измените на нужную)
TARGET_DATE = date(2025, 5, 27)  # 27 мая 2024

async def send_message():
    today = date.today()
    days_left = (TARGET_DATE - today).days

    if days_left > 0:
        message = f"До выхода Султана на свободу осталось {days_left} дней! 🕊️"
    elif days_left == 0:
        message = "Сегодня день выхода Султана на свободу! 🎉"
    else:
        message = "Султан уже на свободе! 🚀"

    bot = Bot(token=TOKEN)
    await bot.send_message(CHAT_ID, message)
    await bot.session.close()

if __name__ == "__main__":
    asyncio.run(send_message())