from enum import Enum
from Film import Film


class WayToCreate(Enum):
    drawn = 1
    puppet = 2
    plasticine = 3


class Cartoon(Film):
    def __init__(self):
        super().__init__()
        self.way_to_create = None

    def read_from(self, stream):
        self.title = stream.readline().rstrip("\n")

        k = int(stream.readline())

        match k:
            case WayToCreate.drawn.value:
                self.way_to_create = WayToCreate.drawn
            case WayToCreate.puppet.value:
                self.way_to_create = WayToCreate.puppet
            case WayToCreate.plasticine.value:
                self.way_to_create = WayToCreate.plasticine
            case _:
                stream.close()
                raise Exception("Error type!")
        self.country = stream.readline().rstrip("\n")

    def write_to(self, stream):
        stream.write(f"Мультфильм.\n"
                     f"\tНазвание: {self.title}\n"
                     f"\tСпособ создания: ")
        k = self.way_to_create

        match k:
            case WayToCreate.drawn:
                stream.write(f"Нарисованный\n")
            case WayToCreate.puppet:
                stream.write(f"Кукольный \n")
            case WayToCreate.plasticine:
                stream.write(f"Пластилиновый\n")
            case _:
                return 0
        stream.write(f"\tСтрана: {self.country}\n")
