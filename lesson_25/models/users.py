from pony.orm import PrimaryKey, Optional

from lesson_25.session import db


class Users(db.Entity):
    id = PrimaryKey(str)
    name = Optional(str)
    age = Optional(int)
    email = Optional(str)
