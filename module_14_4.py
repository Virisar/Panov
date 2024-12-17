import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions import initiate_db, get_all_products  # Импортируем функции

API_TOKEN = 'Токен бота'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание объекта бота
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage)

# Инициализация базы данных и таблицы
initiate_db()


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


@dp.message(lambda message: message.text == "Купить")
async def get_buying_list(message: types.Message):
    products = get_all_products()  # Получаем все продукты из базы данных
    response = "Список товаров:\n"

    for product in products:
        response += f'Название: {product[0]} | Описание: {product[1]} | Цена: {product[2]}\n'

    await message.answer(response)
    await message.answer("Выберите продукт для покупки:", reply_markup=product_keyboard)


@dp.callback_query(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()  # Подтверждение обработки callback


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
