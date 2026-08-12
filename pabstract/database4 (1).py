from abc import ABC, abstractmethod

class Database(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def connect(self):
        pass

    def display_database_name(self):
        print("Database:", self.name)


class MySQL(Database):

    def connect(self):
        print("Connected to MySQL")


database = MySQL("MySQL")

database.connect()
database.display_database_name()