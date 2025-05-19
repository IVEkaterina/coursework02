from typing import Union


class Vacancies:
    """ Что-то очень важное """

    __slots__ = ('name', 'vacancies_url', 'salary', 'description')

    name: str
    vacancies_url: str
    salary: Union[str, int, float]
    description: str

    def __init__(self, name: str, vacancies_url: str, salary: Union[str, int, float], description: str):
        """ sjhdf """
        self.name = name
        self.vacancies_url = vacancies_url
        self.salary = self.__validate_salary(salary)
        self.description = description

    def __validate_salary(self, salary: str):
        """ jkir """
        if salary is None or salary == "":
            return 0
        if isinstance(salary, str):
            cleaned = salary.replace(" ", "").replace("руб.", "").replace("руб", "")
            try:
                if "-" in cleaned:
                    min_sal, max_sal = cleaned.split("-")
                    return (int(min_sal) + int(max_sal)) // 2
                else:
                    return int(cleaned)
            except Exception:
                return 0
        if isinstance(salary, (int, float)):
            return int(salary)
        raise ValueError("Некорректный формат зарплаты")

    def __eq__(self, other):
        """ lkjfg """
        if not isinstance(other, Vacancies):
            return NotImplemented
        return self.salary == other.salary

    def __lt__(self, other):
        """ sdfh """
        if not isinstance(other, Vacancies):
            return NotImplemented
        return self.salary < other.salary

    def __gt__(self, other):
        """ sdj """
        if not isinstance(other, Vacancies):
            return NotImplemented
        return self.salary > other.salary
