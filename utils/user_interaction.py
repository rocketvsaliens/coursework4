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
        if choice == '0' or choice == '':
            print(f'Число должно быть больше 0 и меньше {len(vacancies_list)}')
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


def filter_top_vacancies(handler, top_vacancies):
    filter_words = input('Введите ключевые слова через пробел для фильтрации в топе вакансий\n'
                         'или нажмите Enter, чтобы пропустить этот шаг: ').split()

    if filter_words:
        filtered_list = handler.search_instances_by_keywords(top_vacancies, filter_words)
        if filtered_list:
            print(f'\nОтобрано {len(filtered_list)} вакансий, в которых есть хотя бы одно из ключевых слов\n')
            while True:
                choice = input('Выберите действие: 1 - показать вакансии, 2 - записать вакансии в файл ')
                if choice == '1':
                    for vacancy in filtered_list:
                        print(vacancy)
                        break
                elif choice == '2':
                    save_to_file(handler, filtered_list)
                    exit(0)
                else:
                    print('Некорректный ввод.')
        else:
            print('Нет вакансий, соответствующих заданным критериям.')
    else:
        while True:
            print('Вы не ввели слова для фильтрации. Сохранить топ-вакансий в файл?')
            choice = input('Выберите действие: 0 - выйти из программы, 2 - записать вакансии в файл ')
            if choice == '0':
                print('Всего доброго!')
                break
            elif choice == '2':
                save_to_file(handler, top_vacancies)
                exit(0)
            else:
                print('Некорректный ввод.')


def save_to_file(handler, vacancies_list):
    while True:
        file_format = input('Выберите формат файла: 0 - csv, 1 - xls ')
        filename = input('Введите имя файла (без расширения): ')
        if filename == '':
            filename = 'vacancies'
        if file_format == '0':
            handler.write_vacancies_to_csv(filename, vacancies_list)
            break
        elif file_format == '1':
            handler.write_vacancies_to_xls(filename, vacancies_list)
            break
        else:
            print('Некорректный ввод')
