from src.abstract_saver import VacancySaver
import json
import os


class JsonSaver(VacancySaver):
    JSON_DATA_PATH = os.path.join('..', 'json_data', 'vacancies.json')

    def save_vacancies_to_json(self, vacancy_list):
        """
        Сохраняет вакансии в JSON-файл
        :param vacancy_list: список с вакансиями
        """
        try:
            with open(self.JSON_DATA_PATH, 'w') as file:
                json.dump(vacancy_list, file, indent=2, ensure_ascii=False)
            print("Данные успешно записаны в файл.")
        except Exception as e:
            print(f"Ошибка при записи данных в файл: {e}")

    def load_vacancies(self):
        """Загружает данные из файла с вакансиями"""
        try:
            with open(self.JSON_DATA_PATH, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print("Файл не найден.")
            return None
        except json.JSONDecodeError:
            print("Некорректный формат JSON-файла.")
            return None

    def get_vacancies_by_criteria(self, criteria: list) -> list:
        """
        Возвращает данные о вакансиях по заданным критериям
        :param criteria: критерии для поиска по вакансиям
        """
        try:
            vacancies_data = self.load_vacancies()

            filtered_vacancies = []
            for one_vacancy in vacancies_data:
                for one_criteria in criteria:
                    if one_criteria in str(one_vacancy.values()):
                        if one_vacancy not in filtered_vacancies:
                            filtered_vacancies.append(one_vacancy)

            if not filtered_vacancies:
                print('Вакансии по заданным критериям не найдены')
                return []

            return filtered_vacancies

        except FileNotFoundError:
            print("Файл не найден.")
            return []

        except json.JSONDecodeError:
            print("Некорректный формат JSON-файла.")
            return []

    def clear_json_with_vacancies(self):
        """
        Очищает файл с вакансиями
        """
        try:
            with open(self.JSON_DATA_PATH, 'w') as file:
                file.write('')
            print("Данные успешно удалены из файла.")
        except Exception as e:
            print(f"Ошибка при удалении данных из файла: {e}")


if __name__ == '__main__':
    my_data = [
        {'name': 'python', 'city': 'Москва'},
        {"name": 'Новгородский рабочий', 'city': 'Санкт-Петербург'},
        {'name': 11, 'city': 'Нижний Запупыринск'}
    ]

    json_saver = JsonSaver()
    json_saver.save_vacancies_to_json(my_data)

    loaded_data = json_saver.load_vacancies()
    print(loaded_data)

    filter_criteria = ["Нижний", "Новгород"]

    filtered_results = json_saver.get_vacancies_by_criteria(filter_criteria)
    print(filtered_results)

    json_saver.clear_json_with_vacancies()
