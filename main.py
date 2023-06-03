from engine_classes import HeadHunter, SuperJob
from job_class import Vacancy
from json_manip import JSONSaver
from utils import sort_vacancies, top_vacancies

def user_interaction():
    user_keyword = input("Введите ключевое слово: ")
    platforms = []
    user_input = ""
    #Выбор платформ для поиска вакансий
    while(user_input != "start"):
        user_input = input("""Введите платформы, на которых хотите осуществить поиск вакансий:
HH - для добавления платформы HeadHunter
SJ - для добавления платформы SuperJob
start - для продолжения работы
Ввод: """)
        if user_input.upper() in ["HH", "SJ", "START"]:
            if user_input.upper() == "START":
                if len(platforms) == 0:
                    print("Добавьте хотя бы одну платформу!\n")
                    user_input = ""
            if user_input.upper() == "HH":
                if user_input.upper() not in platforms:
                    platforms.append(user_input.upper())
                    print("Платформа HeadHunter добавлена\n")
                else:
                    print("Платформа уже добавлена\n")
            if user_input.upper() == "SJ":
                if user_input.upper() not in platforms:
                    platforms.append(user_input.upper())
                    print("Платформа SuperJob добавлена\n")
                else:
                    print("Платформа уже добавлена\n")
        else:
            print("Некорректный ввод!\n")
    if "HH" in platforms:
        HeadHunter(user_keyword).get_vacancies()
    if "SJ" in platforms:
        SuperJob(user_keyword).get_vacancies()
    #Создание экземпляра класса JSONSaver (создается файл для записи информации о вакансиях)
    path = "data/test.json"
    saver = JSONSaver(path)
    saver.clear_data_file()
    for vacancy in Vacancy.vacancy_list:
        saver.add_vacancy(vacancy)
    print(f"В файл '{path}' записано {len(saver.open_file(path))} вакансий\n")
    while user_input != "end":
        user_input = input(f"""Выберите команду:
delete - удаляет из файла '{path}' вакансии, в которых не указана зарплата
select - выводит вакансии, с зарплатой не меньше указанной
sort - выводит отсортированный по зарплате список вакансий
top - выводит топ 10 вакансий по зарплате
end - завершение работы программы
Ввод: """).lower()

        if user_input in ["delete", "select", "sort", "top", "end"]:
            if user_input == "delete":
                saver.delete_vacancies()
                print(f"Вакансии без зарплаты удалены из файла '{path}'. "
                      f"Осталось {len(saver.open_file(path))} вакансий.\n")
            if user_input == "select":
                while 1:
                    try:
                        user_input = int(input("Введите размер заработной платы: "))
                    except:
                        print("Введены некорректные данные!\n")
                        continue
                    for vacancy in saver.select_vacancies(user_input):
                        print(vacancy)
                    print()
                    break
            if user_input == "sort":
                Vacancy.vacancy_list.clear()
                for vacancy in saver.open_file(path):
                    Vacancy(vacancy["name"],
                            vacancy["url"],
                            vacancy["currency"],
                            vacancy["salary_from"],
                            vacancy["salary_to"],
                            vacancy["description"])
                sort_vacancies(Vacancy.vacancy_list)
            if user_input == "top":
                Vacancy.vacancy_list.clear()
                for vacancy in saver.open_file(path):
                    Vacancy(vacancy["name"],
                            vacancy["url"],
                            vacancy["currency"],
                            vacancy["salary_from"],
                            vacancy["salary_to"],
                            vacancy["description"])
                top_vacancies(Vacancy.vacancy_list)
            if user_input == "end":
                saver.clear_data_file()
                print("Работа программы завершена! До новых встреч!")
        else:
            print("Введена неверная команда!\n")


if __name__ == '__main__':
    user_interaction()


    # print(Vacancy.currency_dict)

    # sv = JSONSaver("data/test.json")
    # for vacancy in Vacancy.vacancy_list:
    #     print(vacancy.__dict__)
    #     sv.add_vacancy(vacancy)
    # for vac in sv.select_vacancies(10000):
    #     print(vac)
    # sv.clear_data_file()