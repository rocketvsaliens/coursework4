from src.headhunter import HeadHunterAPI
from src.superjob import SuperJobAPI
from src.json_saver import JsonSaver
from src.vacancy import Vacancy
from src.vacancy_handler import VacancyHandler

from utils import user_interaction


def main():
    # Создаём экземпляры классов для работы с API сайтов с вакансиями
    hh_provider = HeadHunterAPI()
    sj_provider = SuperJobAPI()
    # Создаём список экземпляров классов для работы с API сайтов с вакансиями
    platforms = [hh_provider, sj_provider]

    # Создаём экземпляр класса для работы с JSON
    json_saver = JsonSaver()
    # Записываем все полученные вакансии в JSON
    user_interaction.get_search_query_json_data(platforms, json_saver)
    # Удаляем из JSON вакансии без зарплаты
    user_interaction.remove_muddy_vacancies(json_saver)

    # Дальше работаем с экземплярами класса Vacancy
    all_vacancies_list = json_saver.json_to_instances(Vacancy)
    vacancies_handler = VacancyHandler(all_vacancies_list)

    top_vacancies_list = user_interaction.show_top_vacancies_by_salary(vacancies_handler, all_vacancies_list)

    filter_words = input("Введите ключевые слова для фильтрации в топе вакансий: ").split()

    if filter_words:
        filtered_list = vacancies_handler.search_instances_by_keywords(filter_words)
        if filtered_list:
            while True:
                choice = input('Выберите действие: 1 - показать вакансии, 2 - записать вакансии в файл')
                if choice == '1':
                    for vacancy in filtered_list:
                        print(vacancy)
                elif choice == '2':
                    vacancies_handler.write_vacancies_to_xls(filtered_list)
                    break
                else:
                    print('Некорректный ввод')
        else:
            print('Нет вакансий, соответствующих заданным критериям.')

    else:
        while True:
            choice = input('Сохранить топ вакансий в файл? 0 - не сохранять, 1 - сохранить')
            if choice == '0':
                exit(0)
            elif choice == '1':
                vacancies_handler.write_vacancies_to_xls(top_vacancies_list)


if __name__ == '__main__':
    main()
