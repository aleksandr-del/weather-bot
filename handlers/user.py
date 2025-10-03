#!/usr/bin/env python3


from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import Router
from aiogram.filters import CommandStart
from keyboard.keyboard import keyboard
from service.weather_forecast import get_weather_forecast
from filters.filters import CitiesFilter

router = Router(name=__name__)


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text="Узнай прогноз погоды!", reply_markup=keyboard)


@router.message(CitiesFilter())
async def proces_forecast_command(message: Message, api_key: str):
    city = message.text
    text = await get_weather_forecast(api_key, city)
    if text:
        await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(text="Не удалось получить прогноз погоды.")
