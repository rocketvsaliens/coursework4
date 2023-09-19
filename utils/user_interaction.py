def get_search_query_json_data(api_providers, json_instance):
    search_query = input("Введите базовый запрос для поиска вакансии: ")
    # Получаем список с вакансиями
    vacancies_data = []
    for provider in api_providers:
        vacancies_data += provider.get_vacancies_by_api(search_query)

    if not vacancies_data:
        print('К сожалению, не удалось найти вакансии по вашему запросу')
        exit(0)
    else:
        print(f'Получено вакансий: {len(vacancies_data)}\n')
        json_instance.save_vacancies_to_json(vacancies_data)


def remove_muddy_vacancies(json_instance):
    while True:
        choice = input('Удалить вакансии с ненулевой зарплатой. 1 - да, 0 - нет ')
        if choice == '0':
            break
        elif choice == '1':
            json_instance.remove_zero_salary_vacancies()
            break
        else:
            print('Некорректный ввод')


def show_top_vacancies_by_salary(handler, vacancies_list: list) -> list:
    """
    Выводит топ вакансий по зарплате
    :param handler: экземпляр класса-обработчика вакансий
    :param vacancies_list: список вакансий
    :return:
    """
    while True:
        choice = input('\nВведите количество вакансий для вывода в топ N: ')
        if choice == '0':
            break
        else:
            try:
                choice = int(choice)
                if 0 < choice < len(vacancies_list):
                    sorted_vacancies = handler.sort_vacancies_by_salary()[:choice]
                else:
                    sorted_vacancies = handler.sort_vacancies_by_salary()

                highest_paid = sorted_vacancies[0]
                lowest_paid = sorted_vacancies[-1]

                print(f'\nРазбег усреднённых зарплат в этом диапазоне вакансий равен '
                      f'{highest_paid - lowest_paid} руб.\n')

                for vacancy in sorted_vacancies:
                    print(vacancy)
                    print()

                return sorted_vacancies

            except TypeError:
                print('Некорректный ввод. Вакансии не будут показаны.')
                return []
