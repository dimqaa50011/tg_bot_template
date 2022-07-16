from typing import List

from pydantic import BaseModel


class TgBot(BaseModel):
    bot_token: str
    admins: List[int]
    use_redis: bool


class DbConfig(BaseModel):
    user: str
    password: str
    host: str
    database: str
    use_sqlalchemy: bool


class Misk(BaseModel):
    other_params: str = None
