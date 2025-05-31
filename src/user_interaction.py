from src.hh_api import HeadHunterAPI
from src.utils import sort_top_vacancies, search_word_in_description
from pprint import pprint


def user_interaction():
    """ Функция для взаимодействия с пользователем """
    number_vacancy = 1
    hh_api = HeadHunterAPI()

    search_query = input("Введите поисковый запрос: ")

    vacancies = hh_api.load_vacancies(search_query)
    if not vacancies:
        print("По вашему запросу ничего не найдено")
        return

    if not isinstance(vacancies[0], dict):
        print("Ошибка: ожидается список словарей, а получено:", type(vacancies[0]))
        pprint(vacancies)
        return
    for vacancy in vacancies:
        pprint(f"Вакансия номер {number_vacancy}. name: '{vacancy['name']}', vacancies_url: '{vacancy['url']}', salary: '{vacancy['salary']}' ")
        number_vacancy+=1

    while True:
        try:
            top_n = int(input("Введите количество вакансий для вывода в топ N: "))
            break
        except Exception:
            print("Введите число")

    top_vacancies = sort_top_vacancies(vacancies, top_n)
    pprint(top_vacancies)

    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    filter_description = search_word_in_description(vacancies, filter_words)
    pprint(filter_description)

if __name__ == "__main__":
    user_interaction()