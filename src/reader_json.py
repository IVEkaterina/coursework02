import json

from src.file_reader_abc import ReaderABC
from src.vacancies import Vacancies


class ReaderJSON(ReaderABC):
    """ Класс для работы с файлами json формата """

    def __init__(self, file_path="../data/ready_vacancies.json"):
        self.__file_name = file_path

    def __save_vacancies(self, vacancies: Vacancies):
        """ Метод сохранения данных в файл """
        with open(self.__file_name, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, indent=4)

    def __load_vacancies(self):
        """ Метод получения данных из файла """
        with open(self.__file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data

    def delete_vacancy(self, other: Vacancies):
        """ Метод удаления данных из файла """
        data = self.__load_vacancies()
        if other in data:
            data.remove(other)
            self.__save_vacancies(data)

    def add_vacancy(self, other: Vacancies):
        """ Метод добавления данных из файла """
        data = self.__load_vacancies()
        if other not in data:
            data.append(other)
            self.__save_vacancies(data)
