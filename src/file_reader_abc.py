from abc import ABC, abstractmethod # pragma: no cover

class ReaderABC(ABC): # pragma: no cover
    """ Абстрактный класс для работы с файлами """

    @abstractmethod
    def __save_vacancies(self, other):
        """ Абстрактный метод получения добавления данных в файл """
        pass

    @abstractmethod
    def delete_vacancy(self, other):
        """ Абстрактный метод удаления данных из файла """
        pass

    def add_vacancy(self, other):
        """ Абстрактный метод добавления данных из файла """
        pass

    @abstractmethod
    def load_vacancies(self):
        """ Абстрактный метод получения данных из файла """
        pass