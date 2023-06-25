import requests

from src.entities.abstract import Api


class VacancyError(Exception):
    pass


class HeadHunterAPI(Api):

    def __init__(self, keyword: str) -> None:
        self.url = 'https://api.hh.ru/vacancies'
        self.keyword = keyword

    def get_vacancy(self) -> list:
        """
        Получает список вакансий
        """
        try:
            list_vacs = self.get_requests()
        except VacancyError:
            print('Oшибка данных')
        else:
            return self.parsing(list_vacs)

    def get_requests(self) -> list:
        """
        Выполняет запрос по заданным параметрам
        """
        list_response = []
        for page in range(2):
            response = requests.get(self.url, params={
                'name': self.keyword,
                'page': page,
                'per_page': 100})
            if response.status_code != 200:
                raise VacancyError('Oшибка данных')
            list_response.append(response.json()['items'])
        return list_response

    def parsing(self, list_vacs: list) -> list:
        """
        Парсит данные для пользователя
        """
        vacansies = []
        for vacs in list_vacs:
            for vac in vacs:
                salary_from, salary_to = self.get_salary(vac['salary'])
                vacancy = {'vacancy_id': vac['id'],
                           'vacancy_name': vac['name'],
                           'vacancy_city': vac['area']['name'],
                           'vacancy_url': vac['alternate_url'],
                           'salary_from': salary_from,
                           'salary_to': salary_to,
                           'employer_name': vac['employer']['name'],
                           'employer_id': vac['employer']['id']}
                vacansies.append(vacancy)
        return vacansies

    def get_salary(self, salary: dict) -> list:
        """
        Преобразовывает в нужный вид параметр salary
        """
        new_salary = [0, 0]
        if salary and salary['from']:
            new_salary[0] = salary['from']
        if salary and salary['to']:
            new_salary[1] = salary['to']
        return new_salary
