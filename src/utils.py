import re


def sort_top_vacancies(vacancies: list[dict], n: int):
    """ Функция которая возврашвет топ вакансий по зарплате.
    На вход принимает вакансии и желаемое количество вакансий """
    if vacancies:
        def get_salary_from(vacancy):
            salary = vacancy.get("salary")
            if salary and salary.get("from"):
                return salary["from"]
            return 0

        sorted_list = sorted(vacancies, key=get_salary_from, reverse=True)
        result = sorted_list[:n]
        if not result:
            return "По вашему запросу ничего не найдено"
        return result
    return "По вашему запросу ничего не найдено"


def search_word_in_description(vacancies: list[dict], keywords: list[str]):
    """ Функция, котороя принимает вакансии и слово для поиска вакансий с этим словом """
    pattern = re.compile(r"|".join(re.escape(word) for word in keywords), re.I)
    result = []
    for vacancy in vacancies:
        requirement = vacancy["snippet"].get("requirement", "")
        responsibility = vacancy["snippet"].get("responsibility", "")
        description = f"{requirement} {responsibility}".strip()
        if description and pattern.search(description):
            result.append(vacancy)
    if not result:
        return "Не найдено вакансий с таким описанием"
    else:
        return result

