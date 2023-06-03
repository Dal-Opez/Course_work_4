from job_class import Vacancy


def sort_vacancies(list_vacancies: list[Vacancy.vacancy_list]):
    """
    Выводит отсортированные вакансии от большей зарплаты к меньшей
    """
    list_vacancies.sort(reverse=True)
    for vacancy in list_vacancies:
        print(vacancy)


def top_vacancies(list_vacancies: list[Vacancy.vacancy_list]):
    """
    Выводит топ 10 отсортированных зарплат от большей к меньшей
    """
    list_vacancies.sort(reverse=True)
    for i in range(len(list_vacancies) if len(list_vacancies) < 10 else 10):
        print(list_vacancies[i])
