from aiogram.filters import BaseFilter
from aiogram.types import Message


class UserFilter(BaseFilter):
    def __init__(self, user_ids: list[int], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.user_ids = set(user_ids)

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.user_ids


class CitiesFilter(BaseFilter):
    async def __call__(self, message: Message, cities: list[str]):
        return message.text in cities
