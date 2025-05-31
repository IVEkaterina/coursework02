from abc import ABC, abstractmethod # pragma: no cover

class HhApiAbc(ABC): # pragma: no cover
    """ Абстрактный класс для работы с API сервиса с вакансиями. """

    @abstractmethod
    def __connect(self):
        """ Абстрактный метод для подключения к API """
        pass

    @abstractmethod
    def load_vacancies(self, keyword: str):
        """ Абстрактный метод для получения вакансий """
        pass