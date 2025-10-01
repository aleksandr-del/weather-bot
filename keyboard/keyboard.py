#!/usr/bin/env python3


from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from .cities import cities

cities = [KeyboardButton(text=city) for city in cities]
kb_builder = ReplyKeyboardBuilder()
kb_builder.add(*cities)
kb_builder.adjust(2, 1, repeat=True)

keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True)
