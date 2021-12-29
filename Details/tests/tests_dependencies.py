class DetailsPaths:
    def __init__(self):
        self.__STANDARD_BACKEND_URL = 'http://localhost:8000/details'
        self.__DOMAIN_URL = '/domain'
        self.__HIGH_SCHOOL_PROFILE_URL = '/high-school-profile'
        self.__HIGH_SCHOOL_URL = '/high-school'
        self.__TOWN_URL = '/town'
        self.__UNIVERSITY_URL = '/university'
        self.__FACULTY_URL = '/faculty'
        self.__POSITION_URL = '/position'

    def build_domain_url(self):
        return self.__STANDARD_BACKEND_URL + self.__DOMAIN_URL

    def build_high_school_profile_url(self):
        return self.__STANDARD_BACKEND_URL + self.__HIGH_SCHOOL_PROFILE_URL

    def build_high_school_url(self):
        return self.__STANDARD_BACKEND_URL + self.__HIGH_SCHOOL_URL

    def build_town_url(self):
        return self.__STANDARD_BACKEND_URL + self.__TOWN_URL

    def build_university_url(self):
        return self.__STANDARD_BACKEND_URL + self.__UNIVERSITY_URL

    def build_faculty_url(self):
        return self.__STANDARD_BACKEND_URL + self.__FACULTY_URL

    def build_position_url(self):
        return self.__STANDARD_BACKEND_URL + self.__POSITION_URL
