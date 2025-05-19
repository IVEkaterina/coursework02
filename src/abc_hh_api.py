from abc import ABC, abstractmethod

class HhApiAbc(ABC):
    """ Абстрактный класс для работы с API сервиса с вакансиями. """

    @abstractmethod
    def __connect(self):
        """ Абстрактный метод для подключения к API """
        pass

    @abstractmethod
    def load_vacancies(self, word: str):
        """ Абстрактный метод для получения вакансий """
        pass