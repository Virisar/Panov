import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

API_TOKEN = '7695420082:AAFujNs04vOJCR7JJGq_L98eHwCUPdULJoI'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание объекта бота
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher()  # Удалите storage из Dispatcher

# Определение состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Создание клавиатуры
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_calculate, button_info)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Выберите действие:", reply_markup=keyboard)

@dp.message(lambda message: message.text == "Рассчитать")
async def set_age(message: types.Message):
    logging.info("Кнопка 'Рассчитать' нажата")
    await message.answer('Введите свой возраст:')
    await UserState.age.set()  # Установка состояния

@dp.message(UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await state.set_state(UserState.growth)  # Установка состояния

@dp.message(UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await state.set_state(UserState.weight)  # Установка состояния

@dp.message(UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # Формула Миффлина - Сан Жеора для женщин
    calories = 10 * weight + 6.25 * growth - 5 * age + 161

    await message.answer(f'Ваша норма калорий: {calories:.2f}')
    await state.finish()  # Завершение состояния

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
