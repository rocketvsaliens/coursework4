from src.headhunter import HeadHunterAPI
from src.superjob import SuperJobAPI
from src.vacancy import Vacancy

from utils import user_interaction
from utils import vacancies_handler


def main():
    platforms = {'1': 'HeadHunter', '2': 'SuperJob'}

    search_platform = user_interaction.get_started(platforms)

    if search_platform == 'HeadHunter':
        # Создаём экземпляр класса для работы с API HH
        api_provider = HeadHunterAPI()
    else:
        # Создаём экземпляр класса для работы с API SuperJob
        api_provider = SuperJobAPI()

    search_query = input("Введите запрос для поиска вакансии: ")
    vacancies_data = api_provider.get_vacancies_by_api(search_query)

    if not vacancies_data:
        print('Не удалось найти вакансии по вашему запросу')
        exit(0)
    else:
        all_vacancies_list = [Vacancy(i) for i in vacancies_data]
        print(f'Успешно! Получено вакансий: {len(all_vacancies_list)}\n')

    print('Удалить вакансии без указания зарплаты?')
    while True:
        answer = input('Введите "Y", если "да" или "N", если "нет": ').lower()
        if answer not in ('n', 'y'):
            print('Некорректный ввод')
            continue
        elif answer == 'n':
            break
        elif answer == 'y':
            vacancies_with_salary_list = vacancies_handler.filter_by_salary(all_vacancies_list)
            print(f'Успешно! Осталось вакансий: {len(vacancies_with_salary_list)}')
            break


if __name__ == '__main__':
    main()
