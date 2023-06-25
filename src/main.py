from src.entities.hh_api import HeadHunterAPI
from src.config import config
from src.utils import save_data_to_database
from src.entities.DBManager import DBManager


def main():
    # Создаем экземпляры класса для работы с API
    hh_vac = HeadHunterAPI('Python')

    # Получение вакансий
    hh_vacancies = hh_vac.get_vacancy()

    params = config()
    save_data_to_database(hh_vacancies, 'Vacancies_info', params)

    dbmanaer = DBManager(params, 'Vacancies_info')

    print('Привет, что будем выводить?')
    print("""
1 - Список всех компаний и количество вакансий у каждой компании
2 - Список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
3 - Среднюю зарплату по вакансиям
4 - Список всех вакансий, у которых зарплата выше средней по всем вакансиям
5 - писок всех вакансий, в названии которых содержатся переданные в метод 
    """)
    while True:
        user_answer = input('Введи число: ')

        if user_answer == '1':
            emp_info = dbmanaer.get_companies_and_vacancies_count()
            for i in emp_info:
                print(i)

        elif user_answer == '2':
            all_vac = dbmanaer.get_all_vacancies()
            for i in all_vac:
                print(i)

        elif user_answer == '3':
            print(f"Средняя зарплата по вакансии: {dbmanaer.get_avg_salary()}")

        elif user_answer == '4':
            vac = dbmanaer.get_vacancies_with_higher_salary()
            for item in vac:
                print(item)

        elif user_answer == '5':
            keyword = input('Введите ключевое слово: ')
            vac = dbmanaer.get_vacancies_with_keyword(keyword)
            for item in vac:
                print(item)
        else:
            print("Такого варианта нет")

        print("Продолжить работу?")
        answer = input("Y/N")
        if answer == 'N':
            print("Good Bye")
            break


if __name__ == '__main__':
    main()
