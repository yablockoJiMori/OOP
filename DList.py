from Film import Film


class Node:
    def __init__(self, data):
        self.data = data
        self.next = self


class DList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_back(self, item) -> None:
        node = Node(item)

        if self.size == 0:
            self.head = node
            self.tail = node
            self.size += 1
            return

        self.tail.next = node
        node.next = self.head
        self.tail = node
        self.size += 1

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def read_from(self, stream):
        with open(stream, "r", encoding="utf-8") as file_in:
            while line := file_in.readline():
                item = Film.create_from(file_in, line)
                self.push_back(item)

    def write_to(self, stream):
        with open(stream, "a", encoding="utf-8") as file_out:
            file_out.write(f"В контейнере {self.size} элементов.\n")

            for item in self:
                item.write_to(file_out)
                file_out.write(f"\tКоличество гласных: {item.num_vowels()}\n")

    def __iter__(self):
        self.__cur_item = self.head
        self.__flag = 0
        return self

    def __next__(self):
        if self.__flag != self.size:
            self.__flag += 1
            data = self.__cur_item.data
            self.__cur_item = self.__cur_item.next
            return data

        else:
            raise StopIteration
