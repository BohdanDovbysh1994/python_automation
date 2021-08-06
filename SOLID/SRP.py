class MusicAutomat:
    def __init__(self):
        self.__list_of_songs = ["Ace of Base", "Aria", "Led Zeppelin"]
        self.__current_position = 0

    def play_music(self):
        print(self.__list_of_songs[self.__current_position])
        self.__current_position += 1
