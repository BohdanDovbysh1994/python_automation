class TrafficLight:
    def __init__(self, address: str) -> None:
        self.__color = "GREEN"
        self.__address = address
        self.__counter = 0

    def __repr__(self):
        return "I am from repr"

    def __str__(self):
        return (
            f"{self.__class__.__name__}:\n{{\n\tcolor: {self.__color}\n}}"
        )

    def __getattr__(self, item: str):
        return None

    def __getattribute__(self, item: str):
        return super().__getattribute__(item)

    @property
    def color(self):
        return self.__color
