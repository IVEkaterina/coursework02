from src.hh_api import HeadHunterAPI
from src.utils import sort_top_vacancies, search_word_in_description
from pprint import pprint


def user_interaction():

    search_query = input("Введите поисковый запрос: ")

    while True:
        try:
            top_n = int(input("Введите количество вакансий для вывода в топ N: "))
            break
        except Exception:
            print("Введите число")

    filter_words = str(input("Введите ключевые слова для фильтрации вакансий: ").split())

    hh_api = HeadHunterAPI()
    vacancies = hh_api.load_vacancies(search_query)
    pprint(vacancies)

    top_vacancies = sort_top_vacancies(vacancies, top_n)
    pprint(top_vacancies)

    filter_description = search_word_in_description(vacancies, filter_words)
    pprint(filter_description)

if __name__ == "__main__":
    user_interaction()