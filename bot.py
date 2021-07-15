from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils.executor import start_webhook, set_webhook, start_polling
import keyboard as kb
import weather as cc
from config import TOKEN # WEBHOOK_PATH, WEBHOOK_HOST, WEBHOOK_URL, WEBAPP_HOST, WEBAPP_PORT

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def main():
    @dp.message_handler(commands=['start'])
    async def start_command(message: types.Message):
        await message.answer('Привет! Напиши что то!\nПокажу погоду!', reply_markup=kb.cities_kb)

    @dp.message_handler(commands=['help'])
    async def help_command(message: types.Message):
        await message.answer('Покажу тебе погоду в 4 городах Казахстана!\nВыбери город из списка: ', reply_markup=kb.cities_kb)

    @dp.message_handler(commands=['check'])
    async def check_command(message: types.Message):
        await message.answer_photo('https://www.harlingenveterinaryclinic.com/sites/default/files/styles/large/public/golden-retriever-dog-breed-info.jpg?itok=cdghqKxv')

    @dp.message_handler(Text(equals='Жезказган!🏰'))
    async def zhez_weather(message: types.Message):
        now, feels = cc.temperature(cc.zhez_id)
        await message.answer(f'Погода сейчас: {now}°C\nОщущается как: {feels}°C')

    @dp.message_handler(Text(equals='Шымкент!🏜'))
    async def shym_weather(message: types.Message):
        now, feels = cc.temperature(cc.shym_id)
        await message.answer(f'Погода сейчас: {now}°C\nОщущается как: {feels}°C')

    @dp.message_handler(Text(equals='Алматы!⛰'))
    async def ala_weather(message: types.Message):
        now, feels = cc.temperature(cc.almaty_id)
        await message.answer(f'Погода сейчас: {now}°C\nОщущается как: {feels}°C')

    @dp.message_handler(Text(equals='Астана!🏙'))
    async def ast_weather(message: types.Message):
        now, feels = cc.temperature(cc.ast_id)
        await message.answer(f'Погода сейчас: {now}°C\nОщущается как: {feels}°C')

    @dp.message_handler(content_types= types.ContentType.ANY)
    async def simple_message(message: types.Message):
        await message.answer('Извините, я не понимаю.🤔\nПопробуйте /help\nИли возпользуйтесь кнопками!✌️', reply_markup=kb.cities_kb)

    start_polling(dp)

if __name__ == '__main__':
    main()