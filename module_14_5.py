import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions import initiate_db, get_all_products, add_user, is_included  # Импортируем функции

API_TOKEN = 'Токен телеграмм'  #

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
    username = State()  # Добавлено состояние для имени пользователя
    email = State()     # Добавлено состояние для email

# Создание клавиатуры
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
button_buy = KeyboardButton('Купить')
button_register = KeyboardButton('Регистрация')  # Кнопка для регистрации
keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_calculate, button_info, button_buy, button_register)

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

@dp.message(lambda message: message.text == "Регистрация")
async def sign_up(message: types.Message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await UserState.username.set()  # Установка состояния

@dp.message(UserState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if not username.isalpha():  # Проверка на латинские буквы
        await message.answer("Имя пользователя должно содержать только латинские буквы. Введите снова:")
        return

    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя:")
    else:
        await state.update_data(username=username)
        await message.answer('Введите свой email:')
        await UserState.email.set()  # Установка состояния для email

@dp.message(UserState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer('Введите свой возраст:')
    await UserState.age.set()  # Установка состояния для возраста

@dp.message(UserState.age)
async def set_age(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data(age=age)

    data = await state.get_data()
    username = data['username']
    email = data['email']

    # Добавляем пользователя в базу данных
    add_user(username, email, age)
    await message.answer("Регистрация успешна!")

    await state.finish()  # Завершение состояния

@dp.message(lambda message: message.text == "Рассчитать")
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=product_keyboard)

@dp.callback_query(lambda call: call.data == 'product_buying')
async def get_buying_list(call: types.CallbackQuery):
    products = get_all_products()  # Получаем все продукты из базы данных
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