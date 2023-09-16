from abc import ABC, abstractmethod


class VacancyByAPI(ABC):
    """
    Абстрактный класс для работы с платформами для сбора вакансий через API
    """

    @abstractmethod
    def get_vacancies_by_api(self):
        """
        Получает список вакансий по API
        """
        pass

    @staticmethod
    @abstractmethod
    def organize_vacancy_info(vacancy_data: list) -> list:
        pass
