from lesson_10.main import Service


class Repository:
    pass


class UserRepository(Repository):
    pass


class Repository:
    pass


class UserService(Service):
    def __init__(
        self,
        user_repository: Repository
    ):
        self.__user_repository = user_repository


class UserHandler:
    def __init__(
        self,
        user_service: Service
    ):
        self.__user_service = user_service


class UserDepositRepository(Repository):
    pass


if __name__ == '__main__':
    user_repository = UserRepository()
    user_deposit_repository = UserDepositRepository()
    service = UserService(user_deposit_repository)
    handler = UserHandler(service)
