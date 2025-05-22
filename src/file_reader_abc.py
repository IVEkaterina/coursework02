from abc import ABC, abstractmethod

class ReaderABC(ABC):
    """ Абстрактный класс для работы с файлами """

    @abstractmethod
    def save_vacancies(self, other):
        """ Абстрактный метод получения добавления данных в файл """
        pass

    @abstractmethod
    def delete_vacancies(self, other):
        """ Абстрактный метод удаления данных из файла """
        pass

    def add_vacancies(self, other):
        """ Абстрактный метод добавления данных из файла """
        pass

    @abstractmethod
    def read_vacancies(self, other):
        """ Абстрактный метод получения данных из файла """
        pass