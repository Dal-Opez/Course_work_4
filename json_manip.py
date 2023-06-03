from job_class import Vacancy
from abstract_class import VacancySaver
import os
import json


class FileManagerMixin:
    """
    Класс-миксин для работы с json файлом
    """
    @staticmethod
    def _file_existing_check(file_path):
        """
        Проверяет наличие директории и файла, указанных в file_path и осуществляет их создание,
        если те не была найдена
        """
        if not os.path.exists(os.path.dirname(file_path)):
            os.mkdir(os.path.dirname(file_path))
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                file.write(json.dumps([]))

    @staticmethod
    def open_file(file_path):
        """
        Открывает файл и считывает информацию в формате JSON
        """
        with open(file_path, encoding="utf-8") as file:
            return json.load(file)


class JSONSaver(VacancySaver, FileManagerMixin):
    """
    Класс для работы с json файлом: записи, удаления и выбора вакансий
    """
    def __init__(self, file_path):
        self.file_path = file_path

    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, value):
        self.__file_path = value
        self._file_existing_check(self.__file_path)

    def add_vacancy(self, vacancy):
        """
        Добавляет вакансию в json файл
        """
        file_data = self.open_file(self.__file_path)
        file_data.append({"platform": "HH" if "hh.ru" in vacancy.url else "SJ",
                          "name": vacancy.name,
                          "url": vacancy.url,
                          "currency": vacancy.currency,
                          "salary_from": vacancy.salary_from,
                          "salary_to": vacancy.salary_to,
                          "description": vacancy.description})
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(file_data, file, indent=4, ensure_ascii=False)

    def select_vacancies(self, min_salary):
        """
        Осуществляет выбор вакансий по заработной плате
        """
        data_buf = []
        file_data = self.open_file(self.__file_path)
        for vacancy in file_data:
            if vacancy["salary_from"] != 0 and vacancy["salary_from"] != 0:
                if vacancy["salary_from"] >= min_salary or vacancy["salary_to"] >= min_salary:
                    data_buf.append(vacancy)
        Vacancy.vacancy_list.clear()
        for data in data_buf:
            Vacancy(data["name"],
                    data["url"],
                    data["currency"],
                    data["salary_from"],
                    data["salary_to"],
                    data["description"])
        return Vacancy.vacancy_list

    def delete_vacancies(self):
        """
        Удаляет вакансии, в которых не указана зарплата
        """
        data_buf = []
        file_data = self.open_file(self.__file_path)
        for vacancy_data in file_data:
            if vacancy_data["salary_from"] == 0 and vacancy_data["salary_to"] == 0:
                continue
            data_buf.append(vacancy_data)
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(data_buf, file, indent=4, ensure_ascii=False)

    def clear_data_file(self):
        """
        Очищает информацию из json файла
        """
        with open(self.__file_path, "w") as file:
            file.write(json.dumps([]))

