import json

from src.file_reader_abc import ReaderABC
from src.vacancies import Vacancies


class ReaderJSON(ReaderABC):
    """ Класс для работы с файлами json формата """

    def __init__(self, file_path="../data/ready_vacancies.json"):
        self.__file_name = file_path

    def _ReaderABC__save_vacancies(self, vacancies: Vacancies):
        """ Метод сохранения данных в файл """
        with open(self.__file_name, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, indent=4)

    def load_vacancies(self):
        """ Метод получения данных из файла """
        try:
            with open(self.__file_name, "r", encoding="utf-8") as file:
                content = file.read()
                if not content.strip():
                    return []
                return json.loads(content)
        except FileNotFoundError:
            return []

    def delete_vacancy(self, other: Vacancies):
        """ Метод удаления данных из файла """
        if not isinstance(other, Vacancies):
            raise TypeError("Ожидается объект класса Vacancies")
        data = self.load_vacancies()
        if other.to_dict() in data:
            data.remove(other.to_dict())
            self._ReaderABC__save_vacancies(data)

    def add_vacancy(self, other: Vacancies):
        """ Метод добавления данных из файла """
        if not isinstance(other, Vacancies):
            raise TypeError("Ожидается объект класса Vacancies")
        data = self.load_vacancies()
        if other.to_dict() not in data:
            data.append(other.to_dict())
            self._ReaderABC__save_vacancies(data)
