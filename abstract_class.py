from abc import ABC, abstractmethod


class APIEngine(ABC):

    @abstractmethod
    def get_request(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


class VacancySaver(ABC):
    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def select_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass
