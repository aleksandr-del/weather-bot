from dataclasses import dataclass
from environs import Env
from keyboard.cities import cities


@dataclass
class TelegramBot:
    token: str
    user_ids: list[int]


@dataclass
class Weather:
    api_key: str


@dataclass
class Cities:
    cities: list[str]


@dataclass
class Config:
    bot: TelegramBot
    weather: Weather
    cities: Cities


def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(
        bot=TelegramBot(
            token=env("BOT_TOKEN"),
            user_ids=(
                [int(id) for id in env.list("USER_IDS")] if env("USER_IDS") else []
            ),
        ),
        weather=Weather(api_key=env("WEATHER_API_KEY")),
        cities=Cities(cities=cities),
    )
