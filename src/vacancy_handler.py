from src.vacancy import Vacancy


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
                      key=lambda x: x.salary_from, reverse=True)
