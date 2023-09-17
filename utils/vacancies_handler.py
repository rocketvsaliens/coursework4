def filter_by_salary(vacancies: list) -> list:
    """
    Возвращает только вакансии с зарплатой
    """
    return [vacancy for vacancy in vacancies
            if vacancy.get_avg_salary() != 0]
