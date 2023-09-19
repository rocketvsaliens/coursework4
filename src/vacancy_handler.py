import os.path

from src.vacancy import Vacancy
from config import USER_FILE_DIR
import xlwt
import csv


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
                      key=lambda x: x.get_avg_salary(), reverse=True)

    @staticmethod
    def search_instances_by_keywords(list_vacancies, keywords):
        matching_instances = []

        for instance in list_vacancies:
            for key, value in instance.__dict__.items():
                if any(keyword.lower() in str(value).lower() for keyword in keywords):
                    matching_instances.append(instance)
                    break

        return matching_instances

    @staticmethod
    def write_vacancies_to_csv(filename, list_vacancies):
        filename = filename + '.csv'
        file_path = os.path.join(USER_FILE_DIR, filename)

        fieldnames = ['vacancy_title', 'vacancy_area', 'vacancy_url',
                      '_salary_from', '_salary_to', 'currency',
                      'experience', 'requirements']

        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for vacancy in list_vacancies:
                writer.writerow(vars(vacancy))
        print(f'Данные успешно записаны в файл CSV. Путь к файлу: {file_path}')

    @staticmethod
    def write_vacancies_to_xls(filename, list_vacancies):
        filename = filename + '.xls'
        file_path = os.path.join(USER_FILE_DIR, filename)

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

        workbook.save(file_path)
        print(f'Данные успешно записаны в файл XLS. Путь к файлу: {file_path}')
