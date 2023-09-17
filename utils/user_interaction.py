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
