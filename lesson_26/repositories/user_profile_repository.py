from pony.orm import db_session

from lesson_26.session import User


class UserProfileRepository:
    @db_session
    def get_users_with_profiles(self):
        users = User.select()[:]
        for user in users:
            print(user.to_dict())


if __name__ == '__main__':
    repository = UserProfileRepository()
    repository.get_users_with_profiles()
