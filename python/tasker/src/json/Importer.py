import json


class Importer:

    def __init__(self):
        self.database = []

    def read_tasks(self):
        # TODO odczytaj plik i zdekoduj treść tutaj
        with open('taski.json', 'r', encoding='utf-8') as file:
            self.database = json.load(file)

    def get_tasks(self):
        # TODO zwróć zdekodowane taski tutaj
        return self.database