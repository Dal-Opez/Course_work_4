from job_class import Vacancy
from abstract_class import APIEngine
import requests
import os


class HeadHunter(APIEngine):
    """
    Класс для работы с API HeadHunter
    """
    def __init__(self, keyword: str, page=0):
        self.url = "https://api.hh.ru/vacancies"
        self.params = {
            "text": keyword,
            "page": page
        }

    def get_request(self):
        """
        Метод осуществляет поиск по API HeadHunter в соответствии с ключевым словом
        """
        return requests.get(self.url, params=self.params).json()["items"]

    def get_vacancies(self):
        """
        Метод создает экземпляры класса Vacancy
        """
        for vacancy_data in self.get_request():
            Vacancy(vacancy_data["name"],
                    vacancy_data["alternate_url"],
                    vacancy_data["salary"]["currency"] if vacancy_data.get("salary") else None,
                    vacancy_data["salary"]["from"] if vacancy_data.get("salary") else None,
                    vacancy_data["salary"]["to"] if vacancy_data.get("salary") else None,
                    vacancy_data["snippet"]["requirement"])
        print(f"Найдено {len(self.get_request())} вакансий на HeadHunter\n")


class SuperJob(APIEngine):
    """Класс для работы с API SuperJob"""
    def __init__(self, keyword: str, page=1):
        self.url = "https://api.superjob.ru/2.0/vacancies"
        self.params = {
            "keywords": keyword,
            "page": page,
            "area": 113,
        }

    def get_request(self):
        """
        Метод осуществляет поиск по API SuperJob в соответствии с ключевым словом
        """
        headers = {'X-Api-App-Id': os.environ['X-Api-App-Id']}
        return requests.get(self.url, headers=headers, params=self.params).json()["objects"]

    def get_vacancies(self):
        """
        Метод создает экземпляры класса Vacancy
        """
        for vacancy_data in self.get_request():
            Vacancy(vacancy_data["profession"],
                    vacancy_data["link"],
                    vacancy_data["currency"].upper(),
                    vacancy_data["payment_from"],
                    vacancy_data["payment_to"],
                    vacancy_data["type_of_work"]["title"])
        print(f"Найдено {len(self.get_request())} вакансий на SuperJob\n")
