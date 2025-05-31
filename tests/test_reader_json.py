import json
import pytest
from src.reader_json import ReaderJSON
from src.vacancies import Vacancies

@pytest.fixture
def temp_file(tmp_path):
    return tmp_path / "test_vacancies.json"

@pytest.fixture
def reader(temp_file):
    return ReaderJSON(file_path=str(temp_file))

@pytest.fixture
def sample_vacancy():
    return Vacancies(
        name="Python Developer",
        vacancies_url="https://example.com/vacancy",
        salary="100 000-150 000 руб.",
        description="Опыт от 3 лет, знание Python"
    )

def test_add_vacancy_creates_file(reader, sample_vacancy, temp_file):
    reader.add_vacancy(sample_vacancy)

    assert temp_file.exists()

    with open(temp_file, encoding="utf-8") as f:
        data = json.load(f)

    assert sample_vacancy.to_dict() in data

def test_add_vacancy_duplicate_not_added_twice(reader, sample_vacancy):
    reader.add_vacancy(sample_vacancy)
    reader.add_vacancy(sample_vacancy)

    data = reader.load_vacancies()
    assert data.count(sample_vacancy.to_dict()) == 1

def test_delete_vacancy_removes_existing(reader, sample_vacancy):
    reader.add_vacancy(sample_vacancy)
    reader.delete_vacancy(sample_vacancy)

    data = reader.load_vacancies()
    assert sample_vacancy.to_dict() not in data

def test_delete_vacancy_non_existing(reader, sample_vacancy):
    reader.delete_vacancy(sample_vacancy)
    assert reader.load_vacancies() == []

def test_add_vacancy_invalid_type(reader):
    with pytest.raises(TypeError, match="Ожидается объект класса Vacancies"):
        reader.add_vacancy("not a vacancy")

def test_delete_vacancy_invalid_type(reader):
    with pytest.raises(TypeError, match="Ожидается объект класса Vacancies"):
        reader.delete_vacancy({"name": "invalid"})

def test_load_vacancies_empty_file(reader, temp_file):
    temp_file.write_text("")
    assert reader.load_vacancies() == []

def test_load_vacancies_file_not_exist(reader):
    assert reader.load_vacancies() == []
