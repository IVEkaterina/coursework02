import json

from src.abc_hh_api import HhApiAbc
import requests


class HeadHunterAPI(HhApiAbc):
    """ Класс для работы с API HeadHunter и получения вакансий по ключевому слову """

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []
        super().__init__()

    def _HhApiAbc__connect(self):
        """ Отправляет запрос на url api и получает статус """
        response = requests.get(self.__url)
        return True if response.status_code == 200 else False

    def load_vacancies(self, keyword: str):
        """ Метод для получения вакансий по ключевому слову """
        if self._HhApiAbc__connect():
            self.__params['text'] = keyword
            while self.__params.get('page') != 20:
                response = requests.get(self.__url, params=self.__params)
                vacancies = (response.json()).get('items')
                self.__vacancies.extend(vacancies)
                self.__params['page'] += 1
            with open("../data/vacancies.json", "w", encoding="utf-8") as file:
                json.dump(self.__vacancies, file, indent=4)
            if not self.__vacancies:
                return "По вашему запросу ничего найдено"
            return self.__vacancies
        else:
            raise ConnectionError("Где-то какая-то ошибочка")
# gg=HeadHunterAPI()
# print(gg.load_vacancies("Python"))