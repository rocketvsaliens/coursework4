def get_started(platforms: dict) -> str:
    """
    Выбираем платформу для поиска вакансий
    :param platforms: словарь вида {"номер": "платформа вакансий"}
    """
    print('Выберите сайт для поиска вакансий:')
    print(*[f'{i[0]} - {i[1]}' for i in platforms.items()], sep='\n')

    while True:

        platform = input('Введите номер: ')

        search_platform = platforms.get(platform)

        if not search_platform:
            print('Некорректный ввод. Попробуйте снова')
            continue
        else:
            print(f'Выбрана платформа {search_platform}\n')
            break

    return search_platform


def filter_by_non_zero_salary(vacancy_handler) -> list:
    """
    Отфильтровывает вакансии, в которых указана зарплата
    :param vacancy_handler: экземпляр класса-обработчика вакансий
    :return: список с вакансиями, где указана зарплата
    """
    print('Удалить вакансии без указания зарплаты?')
    while True:
        answer = input('0 - "нет", 1 - "да" ')

        if answer == '0':
            return []
        elif answer == '1':
            filtered_vacancy_list = vacancy_handler.remove_without_salary()
            if filtered_vacancy_list:
                print(f'Успешно! Осталось вакансий: {len(filtered_vacancy_list)}\n')
                return filtered_vacancy_list
            else:
                print('Упс! Кажется, для этого запроса не принято указывать зарплату.')
                return []


def show_top_vacancies_by_salary(vacancy_handler, vacancies_list: list) -> None:
    """
    Выводит топ вакансий по зарплате
    :param vacancy_handler: экземпляр класса-обработчика вакансий
    :param vacancies_list: список вакансий
    :return:
    """
    print('Показать топ вакансий по зарплате?')
    while True:
        choice = input('Введите количество вакансий для показа. 0 - не показывать вакансии ')
        if choice == '0':
            break
        else:
            try:
                choice = int(choice)
                if 0 < choice < len(vacancies_list):
                    sorted_vacancies = vacancy_handler.sort_vacancies_by_salary()[:choice]
                else:
                    sorted_vacancies = vacancy_handler.sort_vacancies_by_salary()

                highest_paid = sorted_vacancies[0]
                lowest_paid = sorted_vacancies[-1]

                print(f'\nРазбег усреднённых зарплат вакансий в этом диапазоне равен '
                      f'{highest_paid - lowest_paid} руб.\n')

                for vacancy in sorted_vacancies:
                    print(vacancy)
                    print()
                break

            except TypeError:
                print('Некорректный ввод. Вакансии не будут показаны.')
                break
