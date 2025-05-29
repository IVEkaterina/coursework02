from src.hh_api import HeadHunterAPI
from src.utils import sort_top_vacancies, search_word_in_description
from pprint import pprint


def user_interaction():
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = str(input("Введите ключевые слова для фильтрации вакансий: ").split())

    hh_api = HeadHunterAPI()
    vacancies = HeadHunterAPI.load_vacancies(hh_api, search_query)
    top_vacancies = sort_top_vacancies(vacancies, top_n)
    filter_description = search_word_in_description(vacancies, filter_words)
    pprint(top_vacancies)
    print("."*100)
    pprint(filter_description)

if __name__ == "__main__":
    user_interaction()