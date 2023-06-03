from abc import ABC, abstractmethod


class APIEngine(ABC):
    """
    Абстрактный класс, содержащий прототипы методов для отправки запроса на получение вакансий
    и получения списка вакансий
    """
    @abstractmethod
    def get_request(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


class VacancySaver(ABC):
    """
    Абстрактный класс, содержащий прототипы методов для добавления вакансий, выбора вакансий и
    удаления вакансий
    """
    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def select_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass
