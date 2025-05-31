from src.reader_json import ReaderJSON
from src.user_interaction import user_interaction
from src.vacancies import Vacancies

user_interaction()

vacancy = Vacancies("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")

json_saver = ReaderJSON()
json_saver.add_vacancy(vacancy)
json_saver.delete_vacancy(vacancy)