class AppDependenciesPaths:
    def __init__(self):
        self.__STANDARD_BACKEND_URL = 'http://localhost:8000/app-dependencies'
        self.__HERO_CARD_URL = '/hero-card'
        self.__HOMEWORK_CARD_URL = '/homework-card'
        self.__SCHEDULE_CARD_URL = '/schedule-card'

    def build_hero_card_url(self):
        return self.__STANDARD_BACKEND_URL + self.__HERO_CARD_URL

    def build_homework_card_url(self):
        return self.__STANDARD_BACKEND_URL + self.__HOMEWORK_CARD_URL

    def build_schedule_card_url(self):
        return self.__STANDARD_BACKEND_URL + self.__SCHEDULE_CARD_URL
