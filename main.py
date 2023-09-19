from src.headhunter import HeadHunterAPI
from src.superjob import SuperJobAPI
from src.vacancy import Vacancy
from src.vacancy_handler import VacancyHandler

from utils import user_interaction


def main():
    platforms = {'1': 'HeadHunter', '2': 'SuperJob'}
    # Выбираем платформу для поиска вакансий
    search_platform = user_interaction.get_started(platforms)

    if search_platform == 'HeadHunter':
        # Создаём экземпляр класса для работы с API HH
        api_provider = HeadHunterAPI()
    else:
        # Создаём экземпляр класса для работы с API SuperJob
        api_provider = SuperJobAPI()

    search_query = input("Введите запрос для поиска вакансии: ")
    # Получаем список с вакансиями
    vacancies_data = api_provider.get_vacancies_by_api(search_query)
    # Завершаем программу, если вакансий не найдено
    if not vacancies_data:
        print('К сожалению, не удалось найти вакансии по вашему запросу')
        exit(0)
    else:
        all_vacancies_list = [Vacancy(i) for i in vacancies_data]
        print(f'Успешно! Получено вакансий: {len(all_vacancies_list)}\n')

    # Создаём экземпляр класса для обработки вакансий
    handler = VacancyHandler(all_vacancies_list)

    # Предлагаем пользователю оставить только вакансии с зарплатой
    nonzero_salary_vacancies_list = user_interaction.filter_by_non_zero_salary(handler)
    # Если пользователь оставил только вакансии с зарплатой, предлагаем вывести топ по з\п
    if nonzero_salary_vacancies_list:
        user_interaction.show_top_vacancies_by_salary(handler, nonzero_salary_vacancies_list)

    vacancies_to_file = nonzero_salary_vacancies_list if not nonzero_salary_vacancies_list else all_vacancies_list


if __name__ == '__main__':
    main()
