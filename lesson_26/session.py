from pony.orm import Database, PrimaryKey, Optional, Set, Required
from pony.orm.core import SetData

from lesson_26.entity import Entity

db = Database()
db.bind(provider='postgres', user='postgres', password='postgres', host='localhost', database='mydb')


class User(db.Entity):
    _table_ = "users"

    id = PrimaryKey(str, 8)
    name = Optional(str, 50)
    age = Optional(int)
    email = Optional(str, 25)
    profiles = Set("Profile")

    def to_dict(self):
        data = {}

        for key, value in self._vals_.items():
            if isinstance(value, SetData):
                continue
            data[key.name] = value

        data["profiles"] = []

        for item in self.profiles:
            data["profiles"].append(item.to_dict())

        return data


class Profile(db.Entity):
    _table_ = "profiles"

    id = PrimaryKey(str, 8)
    type = Optional(str, 25)
    country_code = Optional(str, 3)
    user = Required("User", column="user_id")

    def to_dict(self):
        data = {}

        for key, value in self._vals_.items():
            name = key.name

            if name == "user":
                continue

            data[name] = value

        return data


db.generate_mapping(create_tables=False)
