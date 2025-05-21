from src.file_reader_abc import ReaderABC
from src.vacancies import Vacancies


class ReaderJSON(ReaderABC):
    """ Класс для ... """

    def __init__(self, file_name="some.json"):
        """ Конструктор для ... """
        self.__file_name = file_name

    def save_vacancies(self, other: Vacancies):
        """ Метод для ... """
        pass

    def delete_vacancies(self):
        """ Метод для ... """
        pass

    def read_vacancies(self):
        """ Метод для ... """
        pass