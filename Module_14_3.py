import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

API_TOKEN = '7695420082:AAFujNs04vOJCR7JJGq_L98eHwCUPdULJoI'  # Замените на ваш токен

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание объекта бота
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage)  # Создаем диспетчер с хранилищем

# Определение состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Создание клавиатуры
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
button_buy = KeyboardButton('Купить')
keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_calculate, button_info, button_buy)

# Создание Inline-клавиатуры для покупки продуктов
product_keyboard = InlineKeyboardMarkup()
product_keyboard.add(
    InlineKeyboardButton(text='Product1', callback_data='product_buying'),
    InlineKeyboardButton(text='Product2', callback_data='product_buying'),
    InlineKeyboardButton(text='Product3', callback_data='product_buying'),
    InlineKeyboardButton(text='Product4', callback_data='product_buying')
)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Выберите действие:", reply_markup=keyboard)

@dp.message(lambda message: message.text == "Рассчитать")
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=product_keyboard)

@dp.callback_query(lambda call: call.data == 'product_buying')
async def get_buying_list(call: types.CallbackQuery):
    products = [
        ("Product1", "Описание продукта 1", 100),
        ("Product2", "Описание продукта 2", 200),
        ("Product3", "Описание продукта 3", 300),
        ("Product4", "Описание продукта 4", 400)
    ]

    response = "Список товаров:\n"
    for product in products:
        response += f'Название: {product[0]} | Описание: {product[1]} | Цена: {product[2]}\n'

    await call.message.answer(response)
    await call.answer()  # Подтверждение обработки callback

@dp.callback_query(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()  # Подтверждение обработки callback

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
