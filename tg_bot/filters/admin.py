from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class AdminFilter(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin: bool = None):
        self.is_admin = is_admin

    async def check(self, obj: types.Message) -> bool:
        if self.is_admin is None:
            return False
        admins = obj.bot.get('admins')
        return obj.from_user.id in admins
