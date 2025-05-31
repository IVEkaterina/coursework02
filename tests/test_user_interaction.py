import builtins
import pytest
from src.user_interaction import user_interaction
from src.hh_api import HeadHunterAPI


@pytest.fixture
def fake_vacancies():
    return [
        {
            "name": "Python Developer",
            "url": "https://hh.ru/vacancy/123",
            "salary": {"from": 100000},
            "snippet": {
                "requirement": "Опыт с Django",
                "responsibility": "Разработка backend"
            }
        },
        {
            "name": "Junior Developer",
            "url": "https://hh.ru/vacancy/456",
            "salary": {"from": 50000},
            "snippet": {
                "requirement": "Знание Flask",
                "responsibility": "Поддержка приложений"
            }
        }
    ]


def test_user_interaction_with_fake_data(monkeypatch, capsys, fake_vacancies):
    def fake_load_vacancies(self, keyword):
        return fake_vacancies

    monkeypatch.setattr(HeadHunterAPI, "load_vacancies", fake_load_vacancies)

    inputs = iter([
        "python",
        "2",
        "Django Flask"
    ])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    user_interaction()

    output = capsys.readouterr().out

    assert "Python Developer" in output
    assert "Junior Developer" in output
    assert "Django" in output or "Flask" in output
