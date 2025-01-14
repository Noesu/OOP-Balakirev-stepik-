import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for item in data:
            self.lst_data.append({key: value for key, value in zip(self.FIELDS, item.split())})

    def select(self, a, b):
        return self.lst_data[a:b+1]

db = DataBase()
db.insert(lst_in)