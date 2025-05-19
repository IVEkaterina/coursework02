from src.abc_hh_api import HhApiAbc
import requests
from pprint import pprint


class HeadHunterAPI(HhApiAbc):
    """ Класс для чего-то там"""

    def __init__(self):
        """ Конструктор для чего-то там"""
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []
        super().__init__()

    def _HhApiAbc__connect(self):
        """ Отправляет запрос на url api и получает статус"""
        return True if requests.get(self.__url) == 200 else False

    def load_vacancies(self, word: str):
        """ Метод для получения вакансий"""
        if self._HhApiAbc__connect():
            self.__params['text'] = word
            while self.__params.get('page') != 20:
                response = requests.get(self.__url, headers=self.__headers, params=self.__params)
                vacancies = response.json()['items']
                self.__vacancies.extend(vacancies)
                self.__params['page'] += 1
            return self.__vacancies
        else:
            "Где-то какая-то ошибочка"
