from pony.orm import select

from lesson_25.models.users import Users


class UsersRepository:
    def __init__(self):
        self.__model = Users

    def get_all(self):
        print(select(p for p in Users))


if __name__ == '__main__':
    users_repositories = UsersRepository()
    users_repositories.get_all()