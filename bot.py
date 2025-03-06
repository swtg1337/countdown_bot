import os
import asyncio
from datetime import date
from aiogram import Bot

# Берем токен и chat_id из переменных окружения
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Дата освобождения Султана (замени на нужную)
TARGET_DATE = date(2025, 5, 27)  # Например, 27 мая 2024

# Функция для правильного склонения слова "день"
def get_day_word(n):
    if 10 <= n % 100 <= 20:
        return "дней"
    elif n % 10 == 1:
        return "день"
    elif 2 <= n % 10 <= 4:
        return "дня"
    else:
        return "дней"

async def send_message():
    today = date.today()
    days_left = (TARGET_DATE - today).days

    # Правильное склонение в зависимости от числа дней
    day_word = get_day_word(days_left)

    if days_left > 0:
        message = f"До выхода Султана на свободу осталось {days_left} {day_word}! 🕊️"
    elif days_left == 0:
        message = "Сегодня день выхода Султана на свободу! 🎉"
    else:
        message = "Султан уже на свободе! 🚀"

    bot = Bot(token=TOKEN)
    await bot.send_message(CHAT_ID, message)
    await bot.session.close()

if __name__ == "__main__":
    asyncio.run(send_message())