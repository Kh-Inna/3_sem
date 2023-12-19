import random
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

logging.basicConfig(level=logging.INFO)

bot = Bot("6769861804:AAF0qDTpIQA9KH0x-8OMYx5txhExTh_3hzQ")
storage=MemoryStorage()
dp = Dispatcher()

balance = 1

@dp.message(Command("start"))
async def send_start(message: types.Message):
    await message.answer("Guess the color! Type:\n/guess for choose color\n/balance for check your balance\n/rule for read rules")

@dp.message(Command("rule"))
async def send_rules(message: types.Message):
    await message.answer("Rules: \nTry to guess the hidden color by choosing one of three: red, green, blue\nFor a correct answer, plus five points. \nFor an incorrect answer, minus one point.")

@dp.message(Command("balance"))
async def send_balance(message):
    await message.answer(f"Your balance: {balance}")

@dp.message(Command("guess"))
async def choose_color(message: types.Message):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(types.InlineKeyboardButton(text="Red❤️", callback_data="Red❤️"))
    keyboard.add(types.InlineKeyboardButton(text="Green💚", callback_data="Green💚"))
    keyboard.add(types.InlineKeyboardButton(text="Blue💙", callback_data="Blue💙"))
    await message.answer("Choose a color:", reply_markup=keyboard.as_markup())

@dp.callback_query()
async def send_color(call: types.CallbackQuery):
    random_num = random.randint(1, 3)
    if random_num == 1:
        message_1 = 'Red❤️'
    if random_num == 2:
        message_1 = 'Green💚'
    if random_num == 3:
        message_1 = 'Blue💙'
    if (call.data == message_1):
        global balance
        balance += 5
        await call.answer("Correct! +5")
        await call.message.answer(f"Correct answer: {message_1}. Your balance: {balance}")
    elif balance > 1:
        balance -= 1
        await call.answer("Incorrect! -1")
        await call.message.answer(f"Correct answer: {message_1}. Your balance: {balance}")
    elif balance == 1:
        await call.answer("Incorrect!")
        await call.message.answer(f"Correct answer: {message_1}. Your balance: {balance}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())