class Passenger:
    def __init__(
        self,
        name: str,
        place: int,
        start_station: str,
        destination_station: str
    ):
        self.__name = name
        self.__place = place
        self.__start_station = start_station
        self.__destination_station = destination_station

    def __clean_key(self, key: str) -> str:
        return key.replace(f"_{self.__class__.__name__}__", "")

    def __str__(self):
        result = "{\n"

        for key, value in self.__dict__.items():
            result += f"\t{self.__clean_key(key)}: {value}\n"

        return result + "}"
