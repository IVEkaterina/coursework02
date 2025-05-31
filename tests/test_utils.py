import pytest
from src.utils import sort_top_vacancies, search_word_in_description


@pytest.fixture
def sample_vacancies():
    return [
        {
            "name": "Python Developer",
            "salary": {"from": 150000, "to": 200000},
            "snippet": {
                "requirement": "Опыт с Python",
                "responsibility": "Разработка веб-приложений"
            }
        },
        {
            "name": "Java Developer",
            "salary": {"from": 100000, "to": 150000},
            "snippet": {
                "requirement": "Знание Java",
                "responsibility": "Поддержка старых систем"
            }
        },
        {
            "name": "Intern",
            "salary": None,
            "snippet": {
                "requirement": "Желание учиться",
                "responsibility": "Помощь команде"
            }
        },
    ]


def test_sort_top_vacancies_basic(sample_vacancies):
    top = sort_top_vacancies(sample_vacancies, 2)
    assert isinstance(top, list)
    assert len(top) == 2
    assert top[0]["name"] == "Python Developer"
    assert top[1]["name"] == "Java Developer"


def test_sort_top_vacancies_empty_list():
    assert sort_top_vacancies([], 3) == "По вашему запросу ничего не найдено"


def test_sort_top_vacancies_no_salary():
    vacancies = [{"name": "No salary", "salary": None, "snippet": {}}]
    result = sort_top_vacancies(vacancies, 1)
    assert isinstance(result, list)
    assert result[0]["name"] == "No salary"

def test_search(sample_vacancies):
    result = sort_top_vacancies(sample_vacancies, 0)
    assert result == "По вашему запросу ничего не найдено"


def test_search_word_in_description_found(sample_vacancies):
    result = search_word_in_description(sample_vacancies, ["Python"])
    assert isinstance(result, list)
    assert any("Python" in (v["snippet"]["requirement"] + v["snippet"]["responsibility"]) for v in result)


def test_search_word_in_description_case_insensitive(sample_vacancies):
    result = search_word_in_description(sample_vacancies, ["python"])
    assert isinstance(result, list)
    assert len(result) >= 1


def test_search_word_in_description_not_found(sample_vacancies):
    result = search_word_in_description(sample_vacancies, ["Kotlin"])
    assert result == "Не найдено вакансий с таким описанием"


def test_search_word_in_description_empty_vacancies():
    result = search_word_in_description([], ["Python"])
    assert result == "Не найдено вакансий с таким описанием"
