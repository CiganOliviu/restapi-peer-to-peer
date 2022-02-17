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


class AppDependenciesExpectedJsonResponses:
    @staticmethod
    def get_home_content_expected_json_response():
        return {
            'id': 1,
            'config_title': 'Config title',
            'section_one_title_content': {
                    'id': 1,
                    'title': 'Content Section Title One',
                    'content': 'Content Section Content One',
                },
            'section_two_title_content': {
                    'id': 2,
                    'title': 'Content Section Title Two',
                    'content': 'Content Section Content Two',
                },
            'section_one_with_images_content':
                {
                    'id': 1,
                    'image': '/MEDIA/app-layout/ContentWithImages/wallpaper_one.jpg',
                    'title': 'Content Image Section Title One',
                    'content': 'Content Image Section Content One',
                },
            'section_two_with_images_content': {
                    'id': 2,
                    'image': '/MEDIA/app-layout/ContentWithImages/wallpaper_two.jpg',
                    'title': 'Content Image Section Title Two',
                    'content': 'Content Image Section Content Two',
                },
            'section_three_with_images_content': {
                    'id': 3,
                    'image': '/MEDIA/app-layout/ContentWithImages/wallpaper_three.jpg',
                    'title': 'Content Image Section Title Three',
                    'content': 'Content Image Section Content Three',
                }
        }
