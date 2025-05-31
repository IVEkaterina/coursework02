import pytest
from src.vacancies import Vacancies


def test_vacancy_repr():
    vac = Vacancies("Dev", "http://example.com", 100000, "Developer job")
    assert repr(vac) == "Vacancies(name='Dev', salary=100000, url='http://example.com')"


@pytest.mark.parametrize("salary_input,expected", [
    (None, 0),
    ("", 0),
    ("100000", 100000),
    ("100 000", 100000),
    ("100000 руб.", 100000),
    ("100000руб", 100000),
    ("80-120000", 60040),
    ("80 000 - 120 000", 100000),
    ("abc", 0),
    (150000, 150000),
    (150000.5, 150000),
])
def test_validate_salary_various_formats(salary_input, expected):
    vac = Vacancies("Dev", "http://example.com", salary_input, "desc")
    assert vac.salary == expected


def test_to_dict():
    vac = Vacancies("QA Engineer", "http://example.com", "120000", "Тестирование")
    expected = {
        "name": "QA Engineer",
        "url": "http://example.com",
        "salary": 120000,
        "description": "Тестирование",
    }
    assert vac.to_dict() == expected


def test_comparison_equal():
    vac1 = Vacancies("A", "url1", 100000, "desc")
    vac2 = Vacancies("B", "url2", 100000, "desc")
    assert vac1 == vac2


def test_comparison_less_than():
    vac1 = Vacancies("A", "url1", 90000, "desc")
    vac2 = Vacancies("B", "url2", 100000, "desc")
    assert vac1 < vac2
    assert not vac2 < vac1


def test_comparison_greater_than():
    vac1 = Vacancies("A", "url1", 110000, "desc")
    vac2 = Vacancies("B", "url2", 100000, "desc")
    assert vac1 > vac2
    assert not vac2 > vac1


def test_comparison_invalid_type():
    vac = Vacancies("Dev", "url", 100000, "desc")
    assert vac.__eq__(100000) is NotImplemented
    assert vac.__lt__(100000) is NotImplemented
    assert vac.__gt__(100000) is NotImplemented


def test_invalid_salary_type_raises_value_error():
    with pytest.raises(ValueError, match="Некорректный формат зарплаты"):
        Vacancies("Dev", "http://example.com", [""], "description")
