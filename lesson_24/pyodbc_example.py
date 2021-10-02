import psycopg2

from lesson_19.core.page_singleton import singleton


@singleton
class UserRepository:
    def __init__(self):
        self.__connection = psycopg2.connect(
            user="postgres",
            password="postgres",
            host="127.0.0.1",
            port="5432",
            database="mydb"
        )
        self.__cursor = self.__connection.cursor()

    def get_all(self):
        self.__cursor.execute(
            "select * from users;"
        )
        return self.__cursor.fetchall()

    def get_emails(self):
        self.__cursor.execute("select email from users;")
        return self.__cursor.fetchall()

    def update_one_by_email(self, email: str, name: str) -> None:
        self.__cursor.execute(
            f"update users set name = '{name}'"
            f"where users.email = '{email}';"
        )
        self.__connection.commit()

    def __del__(self):
        if self.__connection:
            self.__cursor.close()
            self.__connection.close()


if __name__ == '__main__':
    user_repository = UserRepository()
    print(user_repository.get_all())
    # user_repository.update_one_by_email("john@gmail.com", "Den")
    # print(user_repository.get_all())
