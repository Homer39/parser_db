from abc import ABC, abstractmethod


class Api(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancy(self):
        """
        Получает список вакансий
        """
        pass

    @abstractmethod
    def get_requests(self):
        """
        Выполняет запрос по заданным параметрам
        """
        pass

