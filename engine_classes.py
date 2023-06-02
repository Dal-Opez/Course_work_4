from job_class import Vacancy
from abstract_class import APIEngine
import requests


class HeadHunter(APIEngine):

    def __init__(self, keyword: str, page=0):
        self.url = "https://api.hh.ru/vacancies"
        self.params = {
            "text": keyword,
            "page": page
        }

    def get_request(self):
        print(requests.get(self.url, params=self.params).json()["items"])
        return requests.get(self.url, params=self.params).json()["items"]

    def get_vacancies(self):
        for vacancy_data in self.get_request():
            Vacancy(vacancy_data["name"],
                    vacancy_data["alternate_url"],
                    vacancy_data["salary"]["currency"] if vacancy_data.get("salary") else None,
                    vacancy_data["salary"]["from"] if vacancy_data.get("salary") else None,
                    vacancy_data["salary"]["to"] if vacancy_data.get("salary") else None,
                    vacancy_data["snippet"]["requirement"])
