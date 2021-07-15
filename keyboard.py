from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

buttons = [KeyboardButton('Астана!🏙'), KeyboardButton('Жезказган!🏰'), KeyboardButton('Алматы!⛰'), KeyboardButton('Шымкент!🏜')]

cities_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2).add(*buttons)