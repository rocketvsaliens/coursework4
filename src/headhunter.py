from src.abstract_api import VacancyByAPI
import requests


class HeadHunterAPI(VacancyByAPI):
    """Класс для работы с API HeadHunter"""

    _base_url = "https://api.hh.ru/vacancies"

    def __init__(self, vacancy_title: str, vacancy_area=113, page=0, per_page=50) -> None:
        """
        Конструктор инициализирует экземпляр класса по названию вакансии
        :param vacancy_title: название вакансии
        :param vacancy_area: область поиска -- по умолчанию по всей России
        :param page: страница поиска -- по умолчанию 0 (начальная)
        :param per_page: количество вакансий на страницу -- по умолчанию 50
        """
        self.vacancy_title = vacancy_title
        self.vacancy_area = vacancy_area
        self.page = page
        self.per_page = per_page

    def get_vacancies_by_api(self) -> list[dict] or str:
        """
        Выполняет сбор вакансий через API
        :return: список вакансий для создания экземпляров класса Vacancy
        """
        params = {
            'text': self.vacancy_title,
            'area': self.vacancy_area,
            'page': self.page,
            'per_page': self.per_page
        }
        response = requests.get(self._base_url, params=params)
        if response.status_code == 200:
            vacancies = response.json()['items']

            if vacancies:
                list_vacancies = self.__class__.organize_vacancy_info(vacancies)
                return list_vacancies

        else:
            return f'Ошибка {response.status_code} при выполнении запроса'

    @staticmethod
    def organize_vacancy_info(vacancy_data: list) -> list:
        """
        Организует данные о вакансиях в определённом виде
        :param vacancy_data: список вакансий, полученный через API
        :return: организованный список вакансий
        """

        organized_vacancy_list = []

        for vacancy in vacancy_data:
            name = vacancy.get('name')
            area = vacancy.get('area')['name']
            vacancy_url = f"https://hh.ru/vacancy/{vacancy.get('id')}"
            salary = vacancy.get('salary')
            if not salary:
                salary_from = 0
                salary_to = 0
                currency = ''
            else:
                salary_from = salary.get('from')
                salary_to = salary.get('to')
                if not salary_from:
                    salary_from = salary_to
                if not salary_to:
                    salary_to = salary_from
                currency = vacancy.get('salary')['currency']
            experience = vacancy.get('experience')['name']
            requirements = (vacancy.get('snippet')['requirement'])
            if requirements:
                requirements = requirements.strip().replace('<highlighttext>', '').replace('</highlighttext>', '')

            vacancy_info = {'name': name,
                            'area': area,
                            'vacancy_url': vacancy_url,
                            'salary_from': salary_from,
                            'salary_to': salary_to,
                            'currency': currency,
                            'experience': experience,
                            'requirements': requirements
                            }

            organized_vacancy_list.append(vacancy_info)

        return organized_vacancy_list


if __name__ == '__main__':
    hh = HeadHunterAPI('python')
    print(hh.get_vacancies_by_api())