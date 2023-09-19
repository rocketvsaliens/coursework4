from src.vacancy import Vacancy
from config import XLS_FILE_PATH
import xlwt


class VacancyHandler(Vacancy):
    """Класс для работы со списком вакансий"""

    def __init__(self, vacancies_list):
        self.vacancies_list = vacancies_list

    def remove_without_salary(self) -> list:
        """
        Возвращает только вакансии с зарплатой
        """
        vacancies_with_salary = [vacancy for vacancy in self.vacancies_list
                                 if vacancy.get_avg_salary() != 0]

        return vacancies_with_salary

    def sort_vacancies_by_salary(self) -> list:
        """
        Сортирует вакансии по зарплате
        """
        return sorted(self.remove_without_salary(),
                      key=lambda x: x.salary, reverse=True)

    def search_instances_by_keywords(self, keywords):
        matching_instances = []

        for instance in self.vacancies_list:
            for key, value in instance.__dict__.items():
                if isinstance(value, str) and any(keyword.lower() in value.lower() for keyword in keywords):
                    matching_instances.append(instance)
                    break

        return matching_instances

    @staticmethod
    def write_vacancies_to_xls(list_vacancies):
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('Vacancies')

        fieldnames = ['vacancy_title', 'vacancy_area', 'vacancy_url',
                      'salary_from', 'salary_to', 'currency',
                      'experience', 'requirements']

        # Записываем заголовки полей
        for i, fieldname in enumerate(fieldnames):
            sheet.write(0, i, fieldname)

        # Записываем данные вакансий
        for row, vacancy in enumerate(list_vacancies, start=1):
            for col, fieldname in enumerate(fieldnames):
                value = getattr(vacancy, fieldname, '')
                sheet.write(row, col, value)

        workbook.save(XLS_FILE_PATH)
        print("Данные успешно записаны в файл XLS.")
