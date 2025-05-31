from typing import Union


class Vacancies:
    """ Класс для работы с вакансиями """

    __slots__ = ('name', 'vacancies_url', 'salary', 'description')

    name: str
    vacancies_url: str
    salary: Union[str, int, float]
    description: str

    def __repr__(self):
        return f"Vacancies(name={self.name!r}, salary={self.salary}, url={self.vacancies_url!r})"

    def __init__(self, name: str, vacancies_url: str, salary: Union[str, int, float], description: str):
        """ Конструктор для чего-то там """
        self.name = name
        self.vacancies_url = vacancies_url
        self.salary = self.__validate_salary(salary)
        self.description = description

    @staticmethod
    def __validate_salary(salary: Union[str, int, float]) -> int:
        """ Валидирует и преобразует зарплату к числу """
        if salary is None or salary == "":
            return 0

        if isinstance(salary, str):
            cleaned = salary.replace(" ", "").replace("руб.", "").replace("руб", "").strip()
            if "-" in cleaned:
                parts = cleaned.split("-")
                if len(parts) == 2:
                    try:
                        min_sal = int(parts[0])
                        max_sal = int(parts[1])
                        return (min_sal + max_sal) // 2
                    except ValueError:
                        return 0
                else:
                    return 0
            else:
                try:
                    return int(cleaned)
                except ValueError:
                    return 0

        if isinstance(salary, (int, float)):
            return int(salary)

        raise ValueError("Некорректный формат зарплаты")

    def to_dict(self):
        """ Метод, который возвращает объект класса vacancies словарем """
        return {
            "name": self.name,
            "url": self.vacancies_url,
            "salary": self.salary,
            "description": self.description,
        }

    def __eq__(self, other):
        """ Метод сравнения вакансий """
        if not isinstance(other, Vacancies):
            return NotImplemented
        return self.salary == other.salary

    def __lt__(self, other):
        """ Метод сравнения вакансий """
        if not isinstance(other, Vacancies):
            return NotImplemented
        return self.salary < other.salary

    def __gt__(self, other):
        """ Метод сравнения вакансий """
        if not isinstance(other, Vacancies):
            return NotImplemented
        return self.salary > other.salary
