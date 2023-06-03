import requests


class Vacancy:
    """
    Класс, хранящий информацию о вакансиях
    """
    @staticmethod
    def get_currency():
        """
        Используется для создания словаря с валютами и их курсами по отношению к RUB
        (по какой-то причине валюта BYR не содержится в словаре, поэтому добавление
        производится вручную)
        """
        currency_dict = requests.get("https://open.er-api.com/v6/latest/RUB").json()["rates"]
        currency_dict["BYR"] = 27.7339
        return currency_dict

    currency_dict = get_currency()
    vacancy_list = []

    def __init__(self, name: str, url: str, currency: str, salary_from: int, salary_to: int,  description: str):
        self.name = name
        self.url = url
        self.currency = currency
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.description = description
        self.vacancy_list.append(self)

    def __repr__(self):
        servise = "HH" if "hh.ru" in self.__url else "SJ"
        if self.__currency != "-":
            curren = f"{self.__currency}_to_RUB" if self.__currency != "RUB" else "RUB"
        else:
            curren = "-"
        return f"{servise} - Vacancy({self.__name}, {self.__url}, {curren}, {self.__salary_from}, {self.__salary_to}, {self.__description})"

    def __gt__(self, other):
        average_self = round((self.__salary_from + self.__salary_to) / 2)
        average_other = round((other.__salary_from + other.__salary_to) / 2)
        return average_self > average_other

    def __lt__(self, other):
        average_self = round((self.__salary_from + self.__salary_to) / 2)
        average_other = round((other.__salary_from + other.__salary_to) / 2)
        if average_other == 0:
            return False
        if average_self == 0:
            return True
        return average_self < average_other

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            self.__name = "Наименование вакансии введено в некорректном формате!"

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        if isinstance(value, str):
            self.__url = value
        else:
            self.__url = "Ссылка на вакансию введена в некорректном формате!"

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, value):
        if isinstance(value, str):
            if value == "RUR":
                self.__currency = "RUB"
            else:
                self.__currency = value
        else:
            self.__currency = "-"

    @property
    def salary_from(self):
        return self.__salary_from

    @salary_from.setter
    def salary_from(self, value):
        if self.__currency != '-' and isinstance(value, int):
            if self.currency_dict[self.currency] > 1:
                first = round(value * self.currency_dict[self.currency])
                second = round(first / 1000)
                third = second * 1000
                self.__salary_from = third
                pass
                # self.__salary_from = round(round(value * self.currency_dict[self.currency] / 1000)) * 1000
            else:
                self.__salary_from = round(round(value / self.currency_dict[self.currency] / 1000)) * 1000
        else:
            self.__salary_from = 0

    @property
    def salary_to(self):
        return self.__salary_to

    @salary_to.setter
    def salary_to(self, value):
        if self.__currency != "-" and isinstance(value, int):
            if self.currency_dict[self.currency] > 1:
                self.__salary_to = round(round(value * self.currency_dict[self.currency] / 1000)) * 1000
            else:
                self.__salary_to = round(round(value / self.currency_dict[self.currency] / 1000)) * 1000
        else:
            self.__salary_to = 0

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if isinstance(value, str):
            self.__description = value
        else:
            self.__description = "-"
