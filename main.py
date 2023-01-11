from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from os import getenv

load_dotenv()
getenv('BOT_TOKEN')

bot = Bot(getenv('BOT_TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text=f'Привет, {message.from_user.first_name}, я бот Адам')
    await message.delete()

@dp.message_handler(commands=['picture'])
async def image_handler(message: types.Message):
 photo = open('image/adam.jpg', 'rb')
 await bot.send_photo(message.chat.id, photo=photo)

@dp.message_handler(commands=['myinfo'])
async def get_user_text(message):
    await message.answer(f"Ваш id: {message.from_user.id}\n"
                         f"Ваш first_name:{message.from_user.first_name}!\n"
                         f"Ваш username:{message.from_user.username}!")

@dp.message_handler(commands=['help'])
async def start_command(message: types.Message):
 await message.answer (f"начало: /start\n"
                         f"список команды : /help\n"
                         f"получить информацию: /myninfo\n"
                         f"Показать случайную картину: /picture")


@dp.message_handler()
async def echo(message: types.Message):
    """
       Функция ответа пользователю
    """

    await message.answer(text=message.text)


if __name__ == '__main__':
    executor.start_polling(dp)