from Film import Film


class Documentary(Film):
    def __init__(self):
        super().__init__()
        self.year_of_issue = 0

    def read_from(self, stream):
        self.title = stream.readline().rstrip("\n")
        self.year_of_issue = int(stream.readline())

    def write_to(self, stream):
        stream.write(f"Документальный фильм.\n"
                     f"\tНазвание: {self.title}\n"
                     f"\tГод создания: {self.year_of_issue}\n")