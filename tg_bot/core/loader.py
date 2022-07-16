from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from environs import Env

from .config import DbConfig, Misk, TgBot


class Loader:
    __env = Env()
    __env.read_env()

    __bot_conf = TgBot(
        bot_token=__env.str('BOT_TOKEN'),
        use_redis=__env.str('USE_REDIS'),
        admins=list(map(int, __env.list('ADMINS')))
    )

    __db_conf = DbConfig(
        user=__env.str('DB_USER'),
        password=__env.str('DB_PASS'),
        host=__env.str('DB_HOST'),
        database=__env.str('DB_NAME')
    )

    __misk = Misk()


    @classmethod
    async def load_bot_conf(cls):
        bot = Bot(cls.__bot_conf.bot_token, parse_mode="HTML")
        storage = RedisStorage2 if cls.__bot_conf.use_redis else MemoryStorage
        dp = Dispatcher(bot, storage)
        admins = cls.__bot_conf.admins
        bot["admins"] = admins

        return (bot, dp, storage, admins)

    @classmethod
    async def load_db_config(cls):
        return cls.__db_conf

    @classmethod
    async def load_misk(cls):
        return cls.__misk
