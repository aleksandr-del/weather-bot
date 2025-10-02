#!/usr/bin/env python3


from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import Router, F
from aiogram.filters import CommandStart
from keyboard.keyboard import keyboard
from keyboard.cities import cities
from config.config import Config, load_config
from service.weather_forecast import get_weather_forecast

config: Config = load_config(".env")
router = Router(name=__name__)


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text="Узнай прогноз погоды!", reply_markup=keyboard)


@router.message(F.text.in_(cities))
async def proces_forecast_command(
    message: Message, api_key: str = config.weather.api_key
):
    city = message.text
    text = await get_weather_forecast(api_key, city)
    if text:
        await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(text="Не удалось получить прогноз погоды.")
