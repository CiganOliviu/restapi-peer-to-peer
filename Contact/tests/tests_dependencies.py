class ContactPaths:
    def __init__(self):
        self.__STANDARD_BACKEND_URL = 'http://localhost:8000/contact'
        self.__CONTACT_URL = '/contact-lister'

    def build_contact_url(self):
        return self.__STANDARD_BACKEND_URL + self.__CONTACT_URL
