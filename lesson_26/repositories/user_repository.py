from pony.orm import db_session, select, delete

from lesson_26.session import User


class UserRepository:
    @db_session
    def get_all_with_age_greater_then_row_sql(self, age: int):
        users = User.select_by_sql(
            f"select * from users where age > {age}"
        )
        for user in users:
            print(user)

    @db_session
    def get_all_with_age_greater_then_select_method(self, age: int):
        for user in User.select(lambda user: user.age > age):
            print(user.to_dict())

    @db_session
    def get_all_with_age_greater_then_select_function(self, age: int):
        for user in select(user for user in User if user.age > age):
            print(user.to_dict())

    @db_session
    def get_all(self):
        for user in User.select():
            print(user.to_dict())

    @db_session
    def save(self, data: dict):
        User(**data)

    @db_session
    def delete_one_by_id_with_function(self, id: str):
        delete(user for user in User if user.id == id)

    @db_session
    def delete_one_by_id_with_query_method(self, id: str):
        User.select(lambda user: user.id == id).delete()

    @db_session
    def update_one_by_id(self, id: str, data: dict):
        User.select(lambda user: user.id == id)


if __name__ == '__main__':
    user_repository = UserRepository()
    user_repository.get_all()
    # user_repository.save(
    #     {
    #         "id": "uuuuuuuu",
    #         "name": "Tom",
    #         "age": 100,
    #         "email": "dead.man@gmail.com"
    #     }
    # )
    # user_repository.delete_one_by_id("gggggg")
    # user_repository.delete_one_by_id_with_query_method("uuuuuuuu")
