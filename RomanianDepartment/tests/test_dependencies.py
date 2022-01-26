class RomanianDepartmentPaths:
    def __init__(self):
        self.__STANDARD_BACKEND_URL = 'http://localhost:8000/romanian'
        self.__GROUP_URL = '/romanian-group'
        self.__SCHEDULE_URL = '/romanian-schedule'
        self.__HOMEWORK_URL = '/romanian-homework'

    def build_group_url(self):
        return self.__STANDARD_BACKEND_URL + self.__GROUP_URL

    def build_schedule_url(self):
        return self.__STANDARD_BACKEND_URL + self.__SCHEDULE_URL

    def build_homework_url(self):
        return self.__STANDARD_BACKEND_URL + self.__HOMEWORK_URL
    