import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
import asyncio

API_TOKEN = '7695420082:AAFujNs04vOJCR7JJGq_L98eHwCUPdULJoI'  # Замените на ваш токен

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание объекта бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher()  # Исправлено: убрали storage из Dispatcher

# Определение состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message(Command("calories"))
async def set_age(message: types.Message):
    logging.info("Команда /calories получена")
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message(UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message(UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

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
    await state.finish()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
