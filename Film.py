from Cartoon import Cartoon
from GameFilm import GameFilm
class Film:
    def __init__(self):
        self.title = ""

    def read_from(self, stream):
        pass

    def write_to(self, stream):
        pass

    @staticmethod
    def create_from(stream, line):
        k = int(line)

        match k:
            case 1:
                film = GameFilm()

            case 2:
                film = Cartoon()

            case _:
                stream.close()
                raise Exception("Error type!")

        film.read_from(stream)
        return film