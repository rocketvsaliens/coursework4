from abc import abstractmethod, ABC


class VacancySaver(ABC):
    @abstractmethod
    def save_vacancies_to_json(self, vacancy_list):
        """
        Сохраняет вакансии в JSON-файл
        :param vacancy_list: список с вакансиями
        """
        pass

    @abstractmethod
    def get_vacancies_by_criteria(self, criteria):
        """
        Возвращает данные о вакансиях по заданным критериям
        :param criteria: критерии для поиска по вакансиям
        """
        pass

    @abstractmethod
    def clear_json_with_vacancies(self):
        """
        Очищает файл с вакансиями
        """
        pass
