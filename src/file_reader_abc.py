from abc import ABC, abstractmethod

class ReaderABC(ABC):
    """ Абстрактный класс для ... """

    @abstractmethod
    def save_vacancies(self, other):
        """ Абстрактный метод для ... """
        pass

    @abstractmethod
    def delete_vacancies(self):
        """ Абстрактный метод для ... """
        pass

    @abstractmethod
    def read_vacancies(self):
        """ Абстрактный метод для ... """
        pass