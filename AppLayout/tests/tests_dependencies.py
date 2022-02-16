class AppDependenciesPaths:
    def __init__(self):
        self.__STANDARD_BACKEND_URL = 'http://localhost:8000/app-layout'
        self.__HERO_CARD_URL = '/hero-card'
        self.__HOMEWORK_CARD_URL = '/homework-card'
        self.__SCHEDULE_CARD_URL = '/schedule-card'
        self.__CONTENT_SECTION_URL = '/content-section'
        self.__CONTENT_IMAGE_SECTION_URL = '/content-images-section'
        self.__HOME_CONTENT = '/home-content'

    def build_hero_card_url(self):
        return self.__STANDARD_BACKEND_URL + self.__HERO_CARD_URL

    def build_homework_card_url(self):
        return self.__STANDARD_BACKEND_URL + self.__HOMEWORK_CARD_URL

    def build_schedule_card_url(self):
        return self.__STANDARD_BACKEND_URL + self.__SCHEDULE_CARD_URL

    def build_content_section_url(self):
        return self.__STANDARD_BACKEND_URL + self.__CONTENT_SECTION_URL

    def build_content_image_section_url(self):
        return self.__STANDARD_BACKEND_URL + self.__CONTENT_IMAGE_SECTION_URL

    def build_home_content_url(self):
        return self.__STANDARD_BACKEND_URL + self.__HOME_CONTENT
