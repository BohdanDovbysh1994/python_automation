from lesson_24.sql_alchemy_examples.models.users import Users
from lesson_24.sql_alchemy_examples.session import session


class UsersRepository:
    def __init__(self):
        self.__session = session

    def get_one(self):
        print(self.__session.get(Users, {"id": "aaaaaaaa"}))

    def get_all(self):
        for user in self.__session.query(Users).all():
            print(user)

    def insert_one(self, user: Users):
        self.__session.add(user)
        self.__session.commit()

    def get_one_by_email(self, email: str):
        print(self.__session.query(Users).filter_by(email=email).first())


if __name__ == '__main__':
    users_repository = UsersRepository()
    # users_repository.get_all()
    # users_repository.insert_one(Users(id="gggjjjjj", name="Georgiy", age=50, email="georgiy.dow@gmail.com"))
    # users_repository.get_all()
    users_repository.get_one_by_email("john@gmail.com")
