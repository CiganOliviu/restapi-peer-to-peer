class StatisticsBusinessPaths:
    def __init__(self):
        self.__STANDARD_BACKEND_URL = 'http://localhost:8000/stats'
        self.__CLIENT_URL = '/client'
        self.__TEACHER_URL = '/teacher'
        self.__STAFF_URL = '/staff'
        self.__EXPENSE_URL = '/expense'
        self.__INCOME_URL = '/income'
        self.__FEEDBACK_URL = '/feedback'
        self.__TEACHER_GOAL_URL = '/teacher-expectations'
        self.__STUDENT_EXPECTATIONS_URL = '/student-expectations'

    def build_client_url(self):
        return self.__STANDARD_BACKEND_URL + self.__CLIENT_URL

    def build_teacher_url(self):
        return self.__STANDARD_BACKEND_URL + self.__TEACHER_URL

    def build_staff_url(self):
        return self.__STANDARD_BACKEND_URL + self.__STAFF_URL

    def build_expense_url(self):
        return self.__STANDARD_BACKEND_URL + self.__EXPENSE_URL

    def build_income_url(self):
        return self.__STANDARD_BACKEND_URL + self.__INCOME_URL

    def build_feedback_url(self):
        return self.__STANDARD_BACKEND_URL + self.__FEEDBACK_URL

    def build_teacher_goal_url(self):
        return self.__STANDARD_BACKEND_URL + self.__TEACHER_GOAL_URL

    def build_student_expectations_url(self):
        return self.__STANDARD_BACKEND_URL + self.__STUDENT_EXPECTATIONS_URL
