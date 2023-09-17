class Vacancy:
    """Класс для работы с вакансиями"""

    def __init__(self, vacancy_title: str, vacancy_area: str, vacancy_url: str,
                 salary_from: int, salary_to: int, currency: str,
                 experience: str, requirements: str) -> None:
        """
        Инициализируем экземпляр класса по следующим атрибутам
        :param vacancy_title: название вакансии
        :param vacancy_area: регион
        :param vacancy_url: ссылка на вакансию
        :param salary_from: нижний уровень зарплаты
        :param salary_to: верхний уровень зарплаты
        :param currency: валюта зарплаты
        :param experience: требуемый опыт работы
        :param requirements: требования к вакансии
        """
        try:
            self.vacancy_title = self.validate_string(vacancy_title)
            self.vacancy_area = self.validate_string(vacancy_area)
            self.vacancy_url = self.validate_string(vacancy_url)
            self.salary_from = self.validate_numbers(salary_from)
            self.salary_to = self.validate_numbers(salary_to)
            self.currency = self.validate_string(currency)
            self.experience = self.validate_string(experience)
            self.requirements = self.validate_string(requirements)
        except ValueError:
            self.vacancy_title = 'Неизвестно'
            self.salary_from = self.salary_to = 0
            self.vacancy_area = self.vacancy_url = self.currency \
                = self.experience = self.requirements = None

    def __str__(self) -> str:
        return (
            f'Вакансия: {self.vacancy_title}\n'
            f'<{self.vacancy_url}>\n'
            f'Город/регион: {self.vacancy_area}\n'
            f'Зарплата {self.get_salary_string()}\n'
            f'Опыт работы: {self.experience}\n'
            f'Требования: {self.requirements}\n'
        )

    @staticmethod
    def validate_string(string: str) -> str:
        """Проверка на соответствие строковому типу"""
        if isinstance(string, str):
            return string
        raise ValueError(f'Параметр должен быть строкой')

    @staticmethod
    def validate_numbers(number: int or float) -> int or float:
        """Проверяем, что данные являются числом"""
        if type(number) in (int, float):
            return number
        raise ValueError(f'Параметр должен быть числом')

    def get_currency_info(self) -> str:
        """Преобразуем отображение рублей для зарплаты"""
        if self.currency.lower() in ('rur', 'rub', ''):
            self.currency = 'руб.'
        return self.currency

    def get_salary_string(self) -> str:
        """Формируем строку с зарплатой для метода __str__"""
        if self.get_avg_salary() == 0:
            return 'не указана'
        else:
            return f'{self.salary_from} - {self.salary_to} {self.get_currency_info()}'

    def get_avg_salary(self) -> int:
        """Получаем среднее значение зарплаты для вакансии"""
        avg_salary = int((self.salary_from + self.salary_to) / 2)
        return avg_salary

    @property
    def salary_from(self):
        return self._salary_from

    @salary_from.setter
    def salary_from(self, value):
        self._salary_from = value

    @property
    def salary_to(self):
        return self._salary_to

    @salary_to.setter
    def salary_to(self, value):
        self._salary_to = value


if __name__ == '__main__':
    vc = Vacancy('python', 'Москва', 'http://localhost', 100000, 150000, 'rub', 'Нет', 'Нет')
    print(vc)
