import os
import asyncio
from datetime import date

from aiogram import Bot

# Берем токен и chat_id из переменных окружения
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Дата освобождения Султана (замени на нужную)
TARGET_DATE = date(2025, 5, 27)  # Например, 27 мая 2025

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

# Чтение фактов из файла
def load_facts():
    facts = {}
    with open("facts_per_day.txt", "r", encoding="utf-8") as f:
        for line in f:
            # Разделяем строку на число и факт по первому пробелу
            parts = line.strip().split(" ", 1)  # Разделяем на 2 части: число и факт
            if len(parts) == 2:
                try:
                    days_left = int(parts[0])  # Преобразуем первое число в int
                    fact = parts[1].strip()  # Факт (все после числа)
                    facts[days_left] = fact
                except ValueError:
                    continue  # Игнорируем строки, где нет числа в начале
    return facts

# Функция отправки сообщения
async def send_message():
    today = date.today()
    days_left = (TARGET_DATE - today).days

    # Правильное склонение в зависимости от числа дней
    day_word = get_day_word(days_left)

    # Загружаем факты
    facts = load_facts()

    # Формируем сообщение
    if days_left > 0:
        fact_message = facts.get(days_left, "Факт не найден.")  # Если факта нет для этого дня
        message = f"До выхода Султана на свободу осталось {days_left} {day_word}! 🕊️\n\n{fact_message}"
    elif days_left == 0:
        message = "Сегодня день выхода Султана на свободу! 🎉"
    else:
        message = "Султан уже на свободе! 🚀"

    # Отправляем сообщение в чат
    bot = Bot(token=TOKEN)
    await bot.send_message(CHAT_ID, message)
    await bot.session.close()

if __name__ == "__main__":
    asyncio.run(send_message())
