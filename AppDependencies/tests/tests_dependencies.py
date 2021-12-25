class Constants:
    def __init__(self):
        self.STANDARD_BACKEND_URL = 'http://localhost:8000/app-dependencies'
        self.HERO_CARD_URL = '/hero-card'
        self.HOMEWORK_CARD_URL = '/homework-card'
        self.SCHEDULE_CARD_URL = '/schedule-card'

    def build_hero_card_url(self):
        return self.STANDARD_BACKEND_URL + self.HERO_CARD_URL

    def build_homework_card_url(self):
        return self.STANDARD_BACKEND_URL + self.HOMEWORK_CARD_URL

    def build_schedule_card_url(self):
        return self.STANDARD_BACKEND_URL + self.SCHEDULE_CARD_URL
