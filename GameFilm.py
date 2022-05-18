from Film import Film


class GameFilm(Film):
    def __init__(self):
        super().__init__()
        self.director = ""

    def read_from(self, stream):
        self.title = stream.readline().rstrip("\n")
        self.director = stream.readline().rstrip("\n")
        self.country = stream.readline().rstrip("\n")

    def write_to(self, stream):
        stream.write(f"Игровой фильм.\n"
                     f"\tНазвание: {self.title}\n"
                     f"\tРежиссер: {self.director}\n")
        stream.write(f"\tСтрана: {self.country}\n")
